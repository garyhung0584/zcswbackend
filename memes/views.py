from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from memes.models import Photo
from memes.forms import UploadModelForm

def home(request):
    photos = Photo.objects.all()
    form=UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/memes')
    context={
        'photos':photos,
        'form':form}
    return render(request, 'memes.html', { 'photos' : photos })
def upload(request):
    return render(request, 'upload.html',{
    })
def bpicture(request):
    return render(request, 'picture.html',{
    })