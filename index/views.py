from django.shortcuts import render
from index.models import Photo
from django.views.generic.list import ListView	
# Create your views here.


class GoodListView(ListView):
	template_name = 'main_page/all_photo.html'
	queryset = Photo.objects.all().order_by('date')
	paginator_by = 1 
	cat= None

	def get(self, request, *args, **kwargs):
		return super(GoodListView, self).get(request, *args, **kwargs)

	def get_context_date(self, **kwargs):
		context = super(GoodListView, self).get_context_date(**kwargs)
		context['photos'] = Photo.objects.all().order_by('date')
		return context

	def get_queryset(self):
		return Photo.objects.all().order_by('date')
