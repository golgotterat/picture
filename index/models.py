from django.db import models

# Create your models here.

class Photo(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now=True)
	size = models.IntegerField(null=True)
