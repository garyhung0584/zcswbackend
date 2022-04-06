from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Member(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    username = models.CharField(null=False, blank=True, max_length=16, default='noname')
    intro = models.CharField(default = 'Intro not entered', max_length = 512, blank = True, null = True)
    imguploaded = models.IntegerField(default = 0, null = True)
    likes = models.IntegerField(default = 0, null = True)
    profile_pic = models.ImageField(default = "default.png", blank = True, null = True, upload_to='member/')
    date_create = models.DateTimeField(auto_now_add = True, null = True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    '''
    def __str__(self):
        if self.user:
            return self.user.username
'''