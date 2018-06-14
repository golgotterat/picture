from django.shortcuts import render, get_object_or_404,	redirect 
from index.models import Photo
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect	
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.contrib import messages

# Create your views here.


def PhotoListView(request):
	pag = Paginator(Photo.objects.all().order_by('date'), 1)
	return render(request,'main_page/all_photo.html', {})





# def UploadsPhoto(request, id=None):
# 	#instance = get_object_or_404(Photo, id=id)
# 	instance = Photo()
# 	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		messages.success(request, '<a href="#">Item</a> Saved', extra_tags='html_safe')
# 		return HttpResponseRedirect(request, 'main_page/uploads.html', {})
	
# 	context = {
# 		'form': form,
# 	}

# 	return render(request, 'main_page/uploads.html', context)



def post_detail(request, id):
	instance = get_object_or_404(Photo, id=id)
	img = Photo.objects.get(pk=id)
	return render(request, 'main_page/post_detail.html', {'img': img})





def UploadsPhoto(request, id=None):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		return redirect('post_detail', id=post.pk)
	else:
		form = PostForm()
	return render(request, 'main_page/uploads.html', {'form': form})











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
