from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        pass

    def popular(self):
        pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_user', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='%(app_label)s_%(class)s_related', blank=True)

    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question =  models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)
