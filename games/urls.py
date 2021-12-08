from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='games'),
    path('1', views.game1, name='game1'),
]
