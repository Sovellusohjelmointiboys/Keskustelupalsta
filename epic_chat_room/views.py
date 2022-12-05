from django.shortcuts import render, redirect
from .models import Topic, Reply
from .forms import TopicForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    # The home page for epic chat room
    return render(request, 'epic_chat_room/index.html')


def topics(request):
    # Show all topics
    topics = Topic.objects.order_by('date_modified')
    context = {'topics': topics}
    return render(request, 'epic_chat_room/topics.html', context)

def topic(request, topic_id):
    # Show a single topic and all its entries
    topic = Topic.objects.get(id=topic_id)
    replies = topic.reply_set.order_by('-date_added')
    context = {'topic': topic, 'replies': replies}
    return render(request, 'epic_chat_room/topic.html', context)

@login_required
def new_topic(request):
    #Add a new topic
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('epic_chat_room:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'epic_chat_room/new_topic.html', context)

@login_required
def new_reply(request, topic_id):
    #Add a new reply for a particular topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ReplyForm()
    else:
    # POST data submitted; process data.
        form = ReplyForm(data=request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.owner = request.user
            new_reply.topic = topic
            new_reply.owner = request.user
            new_reply.save()
            return redirect('epic_chat_room:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'epic_chat_room/new_reply.html', context)

@login_required
def edit_reply(request, reply_id):
    # Edit an existing reply
    reply = Reply.objects.get(id=reply_id)
    topic = reply.topic
    # Make sure the topic belongs to the current user.
    if reply.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ReplyForm(instance=reply)
    else:
        # POST data submitted; process data.
        form = ReplyForm(instance=reply, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('epic_chat_room:topic', topic_id=topic.id)

    context = {'reply': reply, 'topic': topic, 'form': form}
    return render(request, 'epic_chat_room/edit_reply.html', context)

@login_required
def delete_reply(request, reply_id):
    reply = Reply.objects.get(id=reply_id)
    topic = reply.topic
    if reply.owner != request.user:
        raise Http404

    if request.method != 'POST':
        reply.delete()
        return redirect('epic_chat_room:topic', topic_id=topic.id)

    context = {}
    return render(request, 'epic_chat_room/delete_reply.html', context)

@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        topic.delete()
        return redirect('epic_chat_room:topics')

    context = {}
    return render(request, 'epic_chat_room/delete_topic.html', context)