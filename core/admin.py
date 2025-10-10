from django.contrib import admin
from .models import Topic, Feedback

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'topic', 'created_at']
    list_filter = ['topic', 'created_at']
    search_fields = ['user_name', 'content']
    readonly_fields = ['created_at']
