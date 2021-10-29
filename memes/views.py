from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from memes.models import Photo
from memes.forms import UploadModelForm

def home(request):
    form=UploadModelForm
    context={'form':form}
    return render(request, 'memes.html', context)
def upload(request):
    return render(request, 'upload.html',{
    })
def bpicture(request):
    return render(request, 'picture.html',{
    })