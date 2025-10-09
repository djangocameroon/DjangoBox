import json
from django.core.management.base import BaseCommand
from core.models import Topic, Feedback

class Command(BaseCommand):
    help = 'Load sample feedback data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, default='data/feedbacks.json')

    def handle(self, *args, **options):
        try:
            with open(options['file'], 'r') as f:
                data = json.load(f)
                
            for item in data:
                topic, _ = Topic.objects.get_or_create(name=item['topic'])
                Feedback.objects.create(
                    user_name=item['user_name'],
                    topic=topic,
                    content=item['content']
                )
                
            self.stdout.write(
                self.style.SUCCESS(f'Successfully loaded {len(data)} feedback entries')
            )
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(f'File {options["file"]} not found')
            )