from typing import Any
from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    name = models.CharField(max_length=4, null=False)
    student_ID = models.CharField(max_length=10)
    question1 = models.CharField(max_length=30, null=False)
    #question2 = models.TextField(null=False)
    trait1 = models.CharField(max_length=10, null=False)
    trait2 = models.CharField(max_length=10, null=False)
    trait3 = models.CharField(max_length=10, null=False)    
    question3 = models.TextField(max_length=30, null=False)
    line_id = models.CharField(max_length=20, default='##########')
    instagram = models.CharField(max_length=20, default='##########')
    
    def __str__(self):
        return self.name