from re import search
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='memes'),
    path('upload', views.photoUpload, name='upload'),
    path('picture/<str:pk>/', views.picture, name='picture'),
    path('filter', views.filter, name='search'),
    path('newTag', views.newTag, name='newTag')
]