
from re import template
import email
from email import message
from email.message import EmailMessage
from re import template
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from memes.models import Photo, Tag, Comment
from memes.forms import UploadModelForm, NewTagForm, CommentForm, ReportForm
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
def photoUpload(request):
    template= 'upload.html'
    if request.method == "GET":
        return render(request, template, {'form':UploadModelForm(initial={'uploader':request.user})})

    if request.method == "POST":
        
        form = UploadModelForm(request.POST, request.FILES, initial={'uploader':request.user})
        print(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/memes')
        else:
            print(form.errors)
            print(form)
            return render(request, template, {'form': form})


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

@csrf_exempt
def newTag(request):
    template = 'upload.html'
    if request.method == "GET":
        return render(request, template, {'form':NewTagForm})
    if request.method == "POST":
        form = NewTagForm(request.POST)
        print(request.POST)
        if form.is_valid():
            tag = form.save()
            return HttpResponse(json.dumps({
                'id': tag.id,
                'name': tag.name,
            }))
        else:
            print(form)
            res = HttpResponse("")
            res.status_code = 400
            return res


@login_required(login_url='login')
def report(request, pk):
    meme = Photo.objects.get(id = pk)
    #post_comments_count = Comment.objects.get(id = pk)
    post_comments = Comment.objects.all().filter(post=Photo.objects.get(id = pk))
    form = CommentForm(initial={'user':request.user,'post': meme})
    if request.method == "GET":
        return render(request, 'picture.html', {
            'meme' : meme,
            'form' : form,
            'post_comments' : post_comments,
            #'post_comments_count' : post_comments_count,
        })
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/memes/picture/'+pk)
    return render(request, 'picture.html',{
        'meme' : meme,
        'form' : form,
        'post_comments' : post_comments,
        #'post_comments_count' : post_comments_count,
    })

def tag(request, pk):
    tag = Tag.objects.get(name = pk)
    return render(request, 'tag.html',{
        'tag' : tag,
    })
    

@login_required(login_url='login')
def report(request, pk):
    meme = Photo.objects.get(id = pk)
    tags = meme.tags.all()
    return render(request, 'picture.html',{
        'meme' : meme,
    })
@login_required(login_url='login')
def delete_picture(request, pk):
    if request.method == 'POST':
        pic = Photo.objects.get(pk)
        pic.delete()
        return HttpResponseRedirect('memes')

@csrf_exempt
def filter(request):
    photo = Photo.objects.all()
 
    filter = Filter(queryset=request.content)
 
    if request.method == "POST":
        filter = Filter(request.POST, queryset=request.content)
 
    
    return render(request, 'filter.html',{
        'photos' : filter
    })