from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from memes.models import Photo
from memes.forms import UploadModelForm

def photoUpload(request):
    photos = Photo.objects.all()
    form=UploadModelForm()
    template= 'upload.html'
    if request.method == "GET":
        return render(request, template, {'memes':UploadModelForm()})

    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/memes')
    context={
        'photos':photos,
        'form':form}
    return render(request, 'memes.html', context)

def home(request):
    return render(request, 'memes.html')

def bpicture(request):
    return render(request, 'picture.html',{
    })