from django.conf.urls import url
from . import views
from index.views import *

# urlpatterns = [
#     url(r'', PhotoListView.as_view(), name='index'),
#     url(r'^/uploads/$', UploadsPhoto.as_view(), name='uploads'),
# ]


urlpatterns = [
    url(r"^(?:(?P<id>\d+)/)?$", views.photo_list_view, name='index'),
    url(r'^img/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^img/(?P<id>\d+)/edit$', views.change_size, name='change_size'),
    url(r'^img/uploads/$',views.uploads_photo, name='uploads'),
]
