from django_unicorn.components import UnicornView
from ..models import Comment
#from django.contrib.auth.models import User

class CommentsView(UnicornView):
    
    #user : User = None
    comments : Comment = None
    content : str = ""
    
    def mount(self):
        #self.user = User.objects.get(user=self.request.User)
        self.comments = Comment.objects.all()
        return super().mount()
        
    def submit(self):
        Comment.objects.create(
            #user = self.user,
            content = self.content
        )
        self.comments = Comment.objects.all()