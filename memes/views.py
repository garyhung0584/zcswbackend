from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
from memes.models import Photo, Tag
from memes.forms import UploadModelForm, NewTagForm
from .filters import Filter
from django.views.decorators.csrf import csrf_exempt 


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
            print("Fuck")
            print(form)
            return render(request, template, {'form': form})

def newTag(request):
    template = 'upload.html'
    if request.method == "GET":
        return render(request, template, {'form':NewTagForm})
    if request.method == "POST":
        form = NewTagForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/memes/upload')
        else:
            print(form)
            return render(request, template, {'form':form})

def home(request):
    photolist = Photo.objects.all()

    return render(request, 'memes.html',{
        'photos' : photolist
    })

def picture(request, pk):
    meme = Photo.objects.get(id = pk)
    tags = meme.tags.all()
    return render(request, 'picture.html',{
        'meme' : meme,
        'tags' : tags
    })

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