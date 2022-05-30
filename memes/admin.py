from django.contrib import admin
from .models import Photo, Tag, Comment, Report
# Register your models here.
admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Report)
