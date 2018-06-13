from django.conf.urls import url
from . import views
from index.views import PhotoListView, UploadsPhoto

# urlpatterns = [
#     url(r'', PhotoListView.as_view(), name='index'),
#     url(r'^/uploads/$', UploadsPhoto.as_view(), name='uploads'),
# ]


urlpatterns = [
    url(r'^$', views.PhotoListView, name='index'),
    url(r'^uploads/(?P<id>)/$',views.UploadsPhoto, name='uploads'),
]
