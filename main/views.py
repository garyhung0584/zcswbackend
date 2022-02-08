from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



from .tokens import account_activation_token
from .models import Member
from .forms import RegisterForm, UserEditForm


def index(request):
    return render(request, 'index.html',{
    })
<<<<<<< HEAD

@login_required(login_url='login')
def userinfo(request):
    return render(request, 'personal_info.html')
        
@login_required(login_url='login')
def useredit(request):
    member = request.user.member
    form = UserEditForm(instance=member)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/main/userinfo')
    
    context = {'form':form}
    return render(request, 'useredit.html', context)
=======
    
def userinfo(request):
    if request.user.is_authenticated:
        return render(request, 'personal_info.html')
    else:
        return HttpResponseRedirect('/accounts/login/')
'''
def useredit(request):
    if request.user.is_authenticated:
        form = UserEditForm()
        if request.method == 'POST':
            form = UserEditForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/main/userinfo/')
        return render(request, 'useredit.html',{
            'form' : form
        })
    else:
        return HttpResponseRedirect('/accounts/login/')
'''
'''
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/main/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/main/')
    else:
            return render(request, 'login.html')
'''
>>>>>>> 021a895 (希望這樣是對的)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_activate_email.html',{
                'user' : user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject,message,to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{
            'form' : form
    })

'''
            auth.login(request,user)
            
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect('/main')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request, 'register.html', {
        'form' : form,
    })
<<<<<<< HEAD
'''
'''
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')'''
        
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        #return HttpResponseRedirect('main')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
=======

def useredit(request):
    member = request.user.member
    form = UserEditForm(instance=member)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'useredit.html', context)
>>>>>>> 021a895 (希望這樣是對的)
