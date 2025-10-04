from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse

from .forms import FeedbackForm
from .models import Topic, Feedback


def feedback_view(request):
    topics = Topic.objects.values_list('name', flat=True)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            topic_name = form.cleaned_data.get('topic')
            topic_obj, _ = Topic.objects.get_or_create(name=topic_name)
            feedback = Feedback(
                user_name=form.cleaned_data['user_name'],
                topic=topic_obj,
                content=form.cleaned_data['content']
            )
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
        {'form': form, 'topics': topics},
    )
