from django import forms
from .models import Photo

class PostForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'photo',  'image_url',)

class ChangeSize(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('photo', 'name', 'photo_width', 'photo_height')