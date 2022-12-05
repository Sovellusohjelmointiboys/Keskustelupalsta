from django import forms
from .models import Topic, Reply

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'text']
        labels = {'title': 'title'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        labels = {'text': 'Reply:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}