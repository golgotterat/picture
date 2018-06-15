from django.shortcuts import render, get_object_or_404,	redirect 
from index.models import Photo
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect	
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm, ChangeSize
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage
from PIL import Image


# Create your views here.








def photo_list_view(request, id):
	#return render(request,'main_page/all_photo.html', {})
	try:
		page_num = request.GET['page']
	except KeyError:
		page_num = 1
	pag = Paginator(Photo.objects.all().order_by('-date'), 6)
	try:
		photo_card = pag.page(page_num)
	except InvalidPage:
		photo_card = pag.page(1)
	return render(request, 'main_page/all_photo.html', {'photo_card': photo_card})


def post_detail(request, id):
	instance = get_object_or_404(Photo, id=id)
	img = Photo.objects.get(pk=id)
	return render(request, 'main_page/post_detail.html', {'img': img})

def uploads_photo(request, id=None):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		print(request.POST)
		post = form.save(commit=False)
		post.save()
		return redirect('post_detail', id=post.pk)
	else:
		form = PostForm()
	return render(request, 'main_page/uploads.html', {'form': form})




def change_size(request, id):
	post = get_object_or_404(Photo, id=id)
	if request.method == "POST":
		print(request.POST)
		# size = (self.photo_height, self.photo_width)
		# image = Image.open(request.POST['photo'])
		# image.show()
		# image.thumbnail(size)
		# image.save('2.png')
		form = ChangeSize(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.change_size_img()
			post.save()
		return redirect('post_detail', id=post.pk)
	else:
		form = ChangeSize(instance=post)
	return render(request, 'main_page/post_change.html', {'form': form})




