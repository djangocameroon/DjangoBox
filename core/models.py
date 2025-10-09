from django.db import models
import markdownfield.models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = markdownfield.models.MarkdownField(rendered_field='content_rendered')
    content_rendered = markdownfield.models.RenderedMarkdownField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user_name} on {self.topic.name}"
