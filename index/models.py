from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.files import File
import os
import urllib.request
from django.core.files.temp import NamedTemporaryFile
# Create your models here.

# class Photo(models.Model):
# 	name = models.CharField(max_length=50)
# 	description = models.TextField(null=True)
# 	date = models.DateTimeField(auto_now=True)
# 	size = models.IntegerField(null=True)

# 	photo_width = models.PositiveSmallIntegerField()
# 	photo_height = models.PositiveSmallIntegerField()
# 	photo = models.ImageField(upload_to='photos/%Y/%m/%d', width_field = 'photo_width', height_field='photo_height')

class Photo(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now=True)	
	photo_width = models.IntegerField(default=0)
	photo_height = models.IntegerField(default=0)
	photo = models.ImageField(width_field ='photo_width', height_field='photo_height', null=True, blank=True)
	#image_file = models.ImageField()
	image_url = models.URLField(null=True, blank=True)
	#photo = models.ImageField(width_field ='photo_width', height_field='photo_height', null=True, blank=True)
	# img_temp = NamedTemporaryFile(delete=True)
	# img_temp.write(urllib.urlopen(url).read())
	# img_temp.flush()
	# im.file.save(img_filename, File(img_temp))

	def get_remote_image(self):
		if self.image_url and not self.photo:
			result = urllib.urlretrieve(self.image_url)
			self.photo.save(os.path.basename(self.image_url), File(open(result[0])))
			self.save()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('index:detail', kwargs={'id': self.id})

	class Meta:
		ordering = ['date']
		verbose_name = 'Изображение'

