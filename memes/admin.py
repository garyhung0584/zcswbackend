from django.contrib import admin
<<<<<<< Updated upstream
from .models import Photo, Tag
=======
from .models import Photo, Tag, Comment, Report
>>>>>>> Stashed changes

# Register your models here.
admin.site.register(Photo)
admin.site.register(Tag)
<<<<<<< Updated upstream
=======
admin.site.register(Comment)
admin.site.register(Report)
>>>>>>> Stashed changes
