from typing import Any
from django.db import models

# Create your models here.

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)
    
    def __str__(self):
        return self.status
    
class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default="不願透漏身分的人")
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
    
class Questionnaire(models.Model):
    name = models.CharField(max_length=4)
    student_ID = models.CharField(max_length=10)
    question1 = models.TextField(null=False)
    question2 = models.TextField(null=False)
    question3 = models.TextField(null=False)
    
    def __str__(self):
        return self.name