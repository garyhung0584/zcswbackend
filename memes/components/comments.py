from django_unicorn.components import UnicornView
from ..models import Comment
from django.contrib.auth.models import User

class CommentsView(UnicornView):
    '''
    comment : Comment = None
    content : str = ""
    
    def mount(self):
        self.member = User.objects.get(user=self.request.User)
        return super().mount()'''
        
    def submit(self):
        Comment.objects.create(
            user = self.user,
            content = self.content
        )