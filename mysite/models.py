from typing import Any
from django.db import models

# Create your models here.
class Questionnaire(models.Model):
    name = models.CharField(max_length=4)
    student_ID = models.CharField(max_length=10)
    question1 = models.TextField(null=False)
    question2 = models.TextField(null=False)
    question3 = models.TextField(null=False)
    
    def __str__(self):
        return self.name