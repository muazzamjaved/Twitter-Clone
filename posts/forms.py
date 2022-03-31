from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields ='__all__'

class PictureForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'