from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def home(request):
    return render(request, 'game selection.html',{
    })
def game1(request):
    return render(request, 'games.html',{
    })