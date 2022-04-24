from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('userinfo', views.userinfo, name='userinfo'),
    path('userinfo/<str:pk>/', views.userinfo, name='userinfo'),
    path('register', views.register, name='register'),
    path('edit/', views.useredit, name='useredit'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'), 
    path('registered/', views.registered, name='registered')
#    path('login', views.login, name='login')
]