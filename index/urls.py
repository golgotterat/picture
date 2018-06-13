from django.conf.urls import url
from index.views import GoodListView

urlpatterns = [
    url(r'', GoodListView.as_view(), name='index'),
]
