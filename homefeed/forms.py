from cloudinary.forms import CloudinaryFileField
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'text', 'image')

    image = CloudinaryFileField(
        options={"folder": "homefeed/",
                 "crop": "limit", "width": 600, "height": 600, }
        )