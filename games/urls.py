from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='games'),
]
urlpatterns = [
    path('', views.game1 name='games'),
]
