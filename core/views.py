from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator

from .forms import FeedbackForm
from .models import Topic, Feedback


def feedback_view(request):
    topics = Topic.objects.values_list('name', flat=True)
    
    # Get all feedbacks for pagination
    feedbacks = Feedback.objects.select_related('topic').order_by('-created_at')
    paginator = Paginator(feedbacks, 10)  # Show 10 feedbacks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            topic_name = form.cleaned_data.get('topic_name')
            topic_obj, _ = Topic.objects.get_or_create(name=topic_name)
            feedback = form.save(commit=False)
            feedback.topic = topic_obj
            feedback.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thank you for your feedback!'})
            messages.success(request, 'Thank you for your feedback!')
            return redirect(reverse('core:home'))
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors.as_json()})
    else:
        form = FeedbackForm()
    
    return render(
        request,
        'core/home.html',
        {'form': form, 'topics': topics, 'page_obj': page_obj},
    )
