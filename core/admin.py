from django.contrib import admin
from .models import Topic, Feedback


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback_count')
    search_fields = ('name',)
    
    def feedback_count(self, obj):
        return obj.feedback_set.count()
    feedback_count.short_description = 'Number of feedbacks'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'topic', 'created_at', 'content_preview')
    list_filter = ('topic', 'created_at')
    search_fields = ('user_name', 'content', 'topic__name')
    readonly_fields = ('created_at', 'content_rendered')
    date_hierarchy = 'created_at'
    
    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content Preview'
