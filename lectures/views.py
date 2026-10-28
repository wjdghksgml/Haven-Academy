from django.shortcuts import render, get_object_or_404
from .models import Topic, Lecture

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'lectures/topic_list.html', {'topics': topics})

def lecture_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    lectures = topic.lectures.all()
    return render(request, 'lectures/lecture_list.html', {'topic': topic, 'lectures': lectures})

def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'lectures/lecture_detail.html', {'lecture': lecture})
