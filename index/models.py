from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
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
	#photo = StdImageField(size=(640, 480))
	photo = models.ImageField(width_field ='photo_width', height_field='photo_height', null=True, blank=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('index:detail', kwargs={'id': self.id})

	class Meta:
		ordering = ['date']
		verbose_name = 'Изображение'