from django.urls import path
from . import views

# Create your URL patterns here.

app_name = 'core'

urlpatterns = [
    path('', views.feedback_view, name='home'),
]