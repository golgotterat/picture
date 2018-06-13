from django.shortcuts import render, get_object_or_404 
from index.models import Photo
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect	
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.contrib import messages
# Create your views here.


def PhotoListView(request):
	return render(request,'main_page/all_photo.html', {})

# def UploadsPhoto(request, id=None):
# 	# instance = get_object_or_404(Post, id=id)
# 	# form = PostForm
# 	return render(request, 'main_page/uploads.html', {})



def SavePhoto(request, id=None):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid(): 
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Created")
		return  HttpResponseRedirect(instance.get_absolute_url())
 	
	context = {
		'form': form,
	}

	return render(request, 'main_page/uploads.html', context)

def UploadsPhoto(request, id=None):
	#instance = get_object_or_404(Photo, id=id)
	instance = Photo()
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, '<a href="#">Item</a> Saved', extra_tags='html_safe')
		return HttpResponseRedirect(request, 'main_page/uploads.html', {})
	
	context = {
		'form': form,
	}

	return render(request, 'main_page/uploads.html', context)

# class PhotoListView(ListView):
# 	template_name = 'main_page/all_photo.html'
# 	queryset = Photo.objects.all().order_by('date')
# 	paginator_by = 1 
# 	cat= None

# 	def get(self, request, *args, **kwargs):
# 		return super(PhotoListView, self).get(request, *args, **kwargs)

# 	def get_context_date(self, **kwargs):
# 		context = super(PhotoListView, self).get_context_date(**kwargs)
# 		context['photos'] = Photo.objects.all().order_by('date')
# 		return context

# 	def get_queryset(self):
# 		return Photo.objects.all().order_by('date')


# class UploadsPhoto(ListView):
# 	template_name = 'main_page/uploads.html'
# 	queryset = Photo.objects.all().order_by('date')
# 	paginator_by = 1 
# 	cat= None

# 	def get(self, request, *args, **kwargs):
# 		return super(UploadsPhoto, self).get(request, *args, **kwargs)

# 	def get_context_date(self, **kwargs):
# 		context = super(UploadsPhoto, self).get_context_date(**kwargs)
# 		context['photos'] = Photo.objects.all().order_by('date')
# 		return context

# 	def get_queryset(self):
# 		return Photo.objects.all().order_by('date')
