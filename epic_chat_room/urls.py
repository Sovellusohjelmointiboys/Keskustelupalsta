# Defines URL patterns for epic_chat_room

from django.urls import path
from . import views

app_name = 'epic_chat_room'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new reply
    path('new_reply/<int:topic_id>/', views.new_reply, name='new_reply'),
    # Page for editing an entry.
    path('edit_reply/<int:reply_id>/', views.edit_reply, name='edit_reply'),
]