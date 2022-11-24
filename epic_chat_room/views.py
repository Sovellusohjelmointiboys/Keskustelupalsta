from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    # The home page for epic chat room
    return render(request, 'epic_chat_room/index.html')

def topics(request):
    # Show all topics
    topics = Topic.objects.order_by('date_modified')
    context = {'topics': topics}
    return render(request, 'epic_chat_room/topics.html', context)