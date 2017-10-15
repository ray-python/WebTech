from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=1)
    author = models.ForeignKey(User, related_name='question_user', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='%(app_label)s_%(class)s_related', blank=True)

    objects = QuestionManager()

    def get_absolute_url(self):
        return ('qa.views.question_details', [str(self.id)])

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, blank=True, null=True)
