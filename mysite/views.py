from django.shortcuts import render, redirect
from mysite import models, forms
from django.core.mail import EmailMessage

def index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    
    message = '如要張貼訊息，則每一個欄位都要填...'
    
    if request.method == 'GET':
        user_id = request.GET.get("user_id")
        user_pass = request.GET.get("user_pass")
        user_post = request.GET.get("user_post")
        user_mood = request.GET.get("mood")
        
        if user_id and user_pass and user_post and user_mood:
            try:
                mood = models.Mood.objects.get(status=user_mood)
                post = models.Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
                post.save()
                message = "成功儲存! 請記得您的編輯密碼【{}】! 訊息經審查後才會顯示。".format(user_pass)
            except models.Mood.DoesNotExist:
                message = "指定的心情不存在。"
        else:
            message = "如要張貼訊息，則每一個欄位都要填..."
    return render(request, 'index_site.html', locals())

def delpost(request, pid=None, del_pass=None):
    if request.method == 'GET':
        if del_pass and pid:
            try:
                post = models.Post.objects.get(id=pid)
                if post.del_pass == del_pass:
                    post.delete()
            except:
                pass
        else:
            message = "輸入錯誤"
    return redirect('/')

def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    message = '如要張貼訊息，則每一個欄位都要填...'
    
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        user_pass = request.POST.get("user_pass")
        user_post = request.POST.get("user_post")
        user_mood = request.POST.get("mood")
        
        if user_id != None:
            mood = models.Mood.objects.get(status=user_mood)
            post = models.Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            message = "成功儲存! 請記得您的編輯密碼【{}】! 訊息經審查後才會顯示。".format(user_pass)
            return redirect('/list/')
    return render(request, 'posting.html',locals())

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

def post2db(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            message = "成功儲存! 訊息經審查後才會顯示。"
            post_form.save()
        else:
            message ='如要張貼訊息，則每一個欄位都要填...'
    else:
        post_form = forms.PostForm()
        message = '如要張貼訊息，則每一個欄位都要填...'
    return render(request, 'post2db.html', locals())