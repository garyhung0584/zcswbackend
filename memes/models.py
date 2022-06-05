from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from rest_framework import serializers
# from rest_framework.serializers import Serializer

class Tag(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=16, null = True)
    # uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null = True)
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL,blank = True, null = True)
    # uploader = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image = models.ImageField(upload_to='memes/', blank = False, null = True)
    upload_date = models.DateTimeField(auto_now_add = True, null = True)
    description = models.TextField(blank = True, max_length = 256, null = True)
    tags = models.ManyToManyField(Tag, blank = True, related_name='photos')
    likes = models.ManyToManyField(User, related_name='likes')
    
    def liker_tuple(self):
        return self.likes.all()

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    post = models.ForeignKey(Photo, related_name="like", on_delete=models.CASCADE, null = True)
    like = models.BooleanField(default= False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    post = models.ForeignKey(Photo, related_name="comments", on_delete=models.CASCADE, null = True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.content[:50]
        #return '%s - %s' % (self.post.title, self.user.username)

class Report(models.Model):
    violence = models.BooleanField(default= False)
    pornography = models.BooleanField(default= False)
    personalattacks = models.BooleanField(default= False)
    hurteyes = models.BooleanField(default= False)
    Jackson = models.BooleanField(default= False)
    content = models.TextField(default= 'Content not entered',blank = True, max_length = 256, null = True)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL,blank = True, null = True)
    post = models.ForeignKey(Photo, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return str(self.post)