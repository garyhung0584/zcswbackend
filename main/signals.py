from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Member

def Member_Profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)

post_save.connect(Member_Profile, sender=User)