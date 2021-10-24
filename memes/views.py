from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from memes.models import Photo

def home(request):
    photos=Photo.objects.all()
    context={'photos':photos}
    return render(request, 'memes.html', context)
def upload(request):
    return render(request, 'upload.html',{
    })
def bpicture(request):
    return render(request, 'picture.html',{
    })