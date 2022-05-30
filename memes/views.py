<<<<<<< Updated upstream
=======
import email
from email import message
from email.message import EmailMessage
from re import template
from django.conf import settings
>>>>>>> Stashed changes
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
from memes.models import Photo
from memes.forms import UploadModelForm
from .models import Photo

<<<<<<< Updated upstream
=======
from memes.models import Photo, Tag
from memes.forms import UploadModelForm, NewTagForm, ReportForm
from .filters import Filter
from django.views.decorators.csrf import csrf_exempt 
import json

def home(request):
    photolist = Photo.objects.all()
    tag = Tag.objects.all()
    return render(request, 'memes.html',{
        'photos' : photolist,
        'tag' : tag
    })

@login_required(login_url='login')
>>>>>>> Stashed changes
def photoUpload(request):
    template= 'upload.html'
    if request.method == "GET":
        return render(request, template, {'form':UploadModelForm()})

    if request.method == "POST":
        
        form = UploadModelForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('/memes')
        else:
            print("Fuck")
            print(form)
<<<<<<< Updated upstream
            return render(request, template, {'form': form})
=======
            res = HttpResponse("")
            res.status_code = 400
            return res


def picture(request, pk):
    meme = Photo.objects.get(id = pk)
    template = 'picture.html'
    form = ReportForm(initial={'reporter':request.user,'post': meme})
    if request.method == "GET":
        return render(request, template, {
            'meme' : meme,
            'form' : form,
        })

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user.email
            mail_subject ='Report successfully'
            message = 'Report successfully'
            to_email = 'jamie44566@gmail.com'
            email = EmailMessage(
                mail_subject,message,settings.EMAIL_HOST_USER,[to_email]
            )
            email.send()
            return redirect('/memes/picture/'+pk)
        else:
            print(form.errors)
            return render(request, template, {'form': form})

    return render(request, 'picture.html',{
        'meme' : meme, 
        'form' : form,
    })
>>>>>>> Stashed changes

def home(request):
    photolist = Photo.objects.all()
    return render(request, 'memes.html',{
        'photos' : photolist
    })

<<<<<<< Updated upstream
def picture(request, pk):
=======
'''
@login_required(login_url='login')
def report(request, pk):
>>>>>>> Stashed changes
    meme = Photo.objects.get(id = pk)
    tags = meme.tags.all()
    return render(request, 'picture.html',{
        'meme' : meme,
        'tags' : tags
    })
'''

def delete_picture(request, pk):
    if request.method == 'POST':
        pic = Photo.objects.get(pk)
        pic.delete()
        return HttpResponseRedirect('memes')