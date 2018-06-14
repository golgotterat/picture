from django import forms
from .models import Photo

class PostForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'photo', 'photo_width', 'photo_height', 'image_url')

class ChangeSize(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('name', 'description')