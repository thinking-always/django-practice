from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"input", "placeholder":"제목"}),
            "content": forms.Textarea(attrs={"class":"textarea", "placeholder": "내용"}),
        }
        labels = {
            "title":"제목",
            "content": "내용",
        }