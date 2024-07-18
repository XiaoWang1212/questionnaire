from django import forms
from mysite import models
class ContactForm(forms.Form):
    
    user_name = forms.CharField(label=" 您的姓名 ", max_length=50, initial=' 李祿 ')
    user_email = forms.EmailField(label=" 電子郵件 ")
    user_message = forms.CharField(label=" 你的意見 ", widget=forms.Textarea)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['mood', 'nickname', 'message', 'del_pass']
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = " 現在心情 "
        self.fields['nickname'].label = " 你的暱稱 "
        self.fields['message'].label = " 心情留言 "
        self.fields['del_pass'].label = " 設定密碼 "