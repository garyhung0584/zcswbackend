from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import auth

def index(request):
    return render(request, 'index.html',{
    })
    
def userinfo(request):
    if request.user.is_authenticated:
        return render(request, 'personal_info.html')
    else:
        return HttpResponseRedirect('/accounts/login/')
<<<<<<< Updated upstream

=======
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
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            return render(request, 'login.html')
=======
            return render(request, 'login.html')
'''

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
<<<<<<< Updated upstream
            user = form.save()
=======
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
            return HttpResponseRedirect('registered')
            #return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{
            'form' : form
    })

def registered(request):
    return render(request, 'registered.html',{
    })

'''
>>>>>>> Stashed changes
            auth.login(request,user)
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect('/main')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request, 'register.html', {
        'form' : form,
    })

def useredit(request):
    member = request.user.member
    form = UserEditForm(instance=member)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'useredit.html', context)
>>>>>>> Stashed changes
