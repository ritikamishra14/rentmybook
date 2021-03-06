from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField( max_length=100)
    pub_date =models.DateTimeField('date published')
    

    def __str__(self):
        return self.question_text

class Choice(models.Model):

    choice_text = models.CharField(max_length=150)
    votes = models.IntegerField(default = 0)
    question =models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
  
 