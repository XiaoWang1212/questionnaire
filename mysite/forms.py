from django import forms
from mysite import models
class ContactForm(forms.Form):
    
    user_name = forms.CharField(label=" 您的姓名 ", max_length=50, initial=' 李祿 ')
    user_email = forms.EmailField(label=" 電子郵件 ")
    user_message = forms.CharField(label=" 你的意見 ", widget=forms.Textarea)
        
class Receive(forms.ModelForm):
    
    class Meta:
        model = models.Questionnaire
        fields = ['name', 'student_ID', 'question1', 'trait1', 'trait2', 'trait3', 'question3', 'line_id', 'instagram']
        
    def __init__(self, *args, **kwargs):
        super(Receive, self).__init__(*args, **kwargs)
        self.fields['name'].label = " 您的名字 "
        self.fields['student_ID'].label = " 您的學號 "
        self.fields['question1'].label = " 第一個問題 "
        self.fields[ 'trait1'].label = " 第一個特質 "
        self.fields[ 'trait2'].label = " 第二個特質 "
        self.fields[ 'trait3'].label = " 第三個特質 "
        self.fields['question3'].label = " 第三個問題 "
        self.fields['line_id'].label = " Line "
        self.fields['instagram'].label = " IG "
        
    def clean(self):
        cleaned_data = super().clean()
        line_id = cleaned_data.get('line_id')
        instagram = cleaned_data.get('instagram')
        
        if not line_id and not instagram:
            raise forms.ValidationError("聯絡方式至少要填一個喔~")
        
        return cleaned_data