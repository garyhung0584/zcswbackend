from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=16, null = True)
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    image = models.ImageField(upload_to='memes/', blank = False, null = True)
    upload_date = models.DateTimeField(auto_now_add = True, null = True)
    description = models.TextField(blank = True, max_length = 256, null = True)
<<<<<<< Updated upstream
    tags = models.ManyToManyField(Tag, blank = True)
    

    def __str__(self):
        return self.title
=======
    tags = models.ManyToManyField(Tag, blank = True, related_name="photos")

    def __str__(self):
        return self.title

class Comment(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #post = models.ForeignKey(Photo, related_name="comments", on_delete=models.CASCADE)
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
>>>>>>> Stashed changes
