import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Votes(models.Model):
    models.IntegerField(default = 0)

class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.answer_text
