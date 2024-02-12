from .models import Post,comment
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields={'title','image','caption'}
        
        
        
class Commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('body','posted_by',)