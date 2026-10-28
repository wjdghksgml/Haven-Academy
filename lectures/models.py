from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lecture(models.Model):
    topic = models.ForeignKey(Topic, related_name='lectures', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_url = models.URLField()

    def __str__(self):
        return self.title
