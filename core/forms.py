from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    topic = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 bg-slate-800 text-white border-blue-700 focus:border-indigo-400 focus:ring-indigo-400 rounded-xl shadow-sm focus:outline-none',
            'placeholder': 'Select or enter a topic',
            'list': 'topic-list',
            'autocomplete': 'off',
        })
    )

    class Meta:
        model = Feedback
        fields = ['user_name', 'topic', 'content']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'block w-full px-3 py-2 bg-slate-800 text-white border-blue-700 focus:border-indigo-400 focus:ring-indigo-400 rounded-xl shadow-sm focus:outline-none',
                'placeholder': 'Your Name',
            }),
            'content': forms.Textarea(attrs={
                'class': 'block w-full px-3 py-2 bg-slate-800 text-white border-blue-700 focus:border-indigo-400 focus:ring-indigo-400 rounded-xl shadow-sm focus:outline-none',
                'placeholder': 'Your feedback...',
                'rows': 6,
            }),
        }
