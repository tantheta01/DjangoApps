from django.db import models
from django.utils import timezone

import datetime

class Question(models.Model):

    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text
    
    def recentpub(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choices(models.Model):

    choice_text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    
