from django import forms
from mysite import models
class ContactForm(forms.Form):
    
    user_name = forms.CharField(label=" 您的姓名 ", max_length=50, initial=' 李祿 ')
    user_email = forms.EmailField(label=" 電子郵件 ")
    user_message = forms.CharField(label=" 你的意見 ", widget=forms.Textarea)
        
class Receive(forms.ModelForm):
    
    class Meta:
        model = models.Questionnaire
        fields = ['name', 'student_ID', 'question1', 'question2', 'question3']
        
    def __init__(self, *args, **kwargs):
        super(Receive, self).__init__(*args, **kwargs)
        self.fields['name'].label = " 您的名字 "
        self.fields['student_ID'].label = " 您的學號 "
        self.fields['question1'].label = " 第一個問題 "
        self.fields['question2'].label = " 第二個問題 "
        self.fields['question3'].label = " 第三個問題 "