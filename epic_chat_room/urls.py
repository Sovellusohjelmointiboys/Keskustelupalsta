# Defines URL patterns for epic_chat_room

from django.urls import path
from . import views

app_name = 'epic_chat_room'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all the topics
    path('topics/', views.topics, name='topics'),
]