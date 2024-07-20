from django.contrib import admin
from mysite import models
# Register your models here.
class PostReply(admin.ModelAdmin):
    list_display = ('name', 'student_ID', 'question1', 'question2', 'question3')

admin.site.register(models.Questionnaire, PostReply)

admin.site.site_header = "後台管理(請回前頁填問卷)"
admin.site.site_title = "後台管理"
admin.site.index_title = "後台管理"