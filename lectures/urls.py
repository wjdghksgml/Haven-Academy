from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('topics/<int:topic_id>/', views.lecture_list, name='lecture_list'),
    path('lectures/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
]
