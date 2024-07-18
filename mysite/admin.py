from django.contrib import admin
from mysite import models
# Register your models here.
class PostReply(admin.ModelAdmin):
    list_display = ('name', 'student_ID', 'question1', 'question2', 'question3')

admin.site.register(models.Questionnaire, PostReply)