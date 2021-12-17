from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
from memes.models import Photo
from memes.forms import UploadModelForm
from .models import Photo

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
            return render(request, template, {'form': form})

def home(request):
    photolist = Photo.objects.all()
    return render(request, 'memes.html',{
        'memes' : photolist
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