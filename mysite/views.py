from django.shortcuts import render, redirect
from mysite import models, forms
from django.core.mail import EmailMessage

def post(request, slug=None):    
    questionnaires = models.Questionnaire.objects.all()
    return render(request, 'post.html', locals())

def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = '感謝您的聯繫!'
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            
            mail_body = u'''
            網友姓名{}
            電子郵件{}
            反應意見 : 如下
            {}'''.format(user_name, user_email, user_message)
            
            email = EmailMessage( '來自【靠背中央】網站的網友意見',
                                 mail_body,
                                 user_email,
                                 ['danny20041212@gmail.com'])
            email.send()
        else:
            message = '請檢查您輸入的資訊是否正確!'
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', locals())

def fillQA(request):
    if request.method == 'POST':
        QA_form = forms.Receive(request.POST)
        student_ID = request.POST.get('student_ID')

        # 檢查學號是否早已存在
        if models.Questionnaire.objects.filter(student_ID=student_ID).exists():
            message = "該學號已填寫過，不能填寫了喔 ! (如有問題請通知管理員)"
        else:
            if QA_form.is_valid():
                form_data = QA_form.cleaned_data
                line_id = form_data.get('line_id') or '##########'
                instagram = form_data.get('instagram') or '##########'

                questionnaire = QA_form.save(commit=False)
                questionnaire.line_id = line_id
                questionnaire.instagram = instagram
                questionnaire.save()
                
                return redirect('thanks')
            else:
                message = QA_form.errors.as_text()
    else:
        QA_form = forms.Receive()
        message = "每個問題都要填寫喔~"
    return render(request, 'fillQA.html', locals())

def thanks(request):
    return render(request, 'thanks.html', locals())