from .models import Photo, Tag
import django_filters

class Filter(django_filters.FilterSet):
 
    class Meta:
        model = Photo
        fields = ('title', 'description', 'tags')