from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Topic, Feedback
import json
import os
from datetime import datetime


class Command(BaseCommand):
    help = 'Import feedback data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/feedbacks.json',
            help='Path to JSON file containing feedback data'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        
        if not os.path.exists(file_path):
            self.stdout.write(
                self.style.ERROR(f'File {file_path} does not exist')
            )
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            imported_count = 0
            for item in data:
                # Get or create topic
                topic, created = Topic.objects.get_or_create(
                    name=item['topic']
                )
                
                # Parse datetime if it exists
                created_at = timezone.now()
                if 'created_at' in item:
                    try:
                        created_at = datetime.fromisoformat(
                            item['created_at'].replace('Z', '+00:00')
                        )
                    except ValueError:
                        pass

                # Create feedback
                feedback, created = Feedback.objects.get_or_create(
                    user_name=item['user_name'],
                    topic=topic,
                    content=item['content'],
                    defaults={'created_at': created_at}
                )
                
                if created:
                    imported_count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully imported {imported_count} feedback entries'
                )
            )

        except json.JSONDecodeError:
            self.stdout.write(
                self.style.ERROR('Invalid JSON file')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error importing data: {str(e)}')
            )