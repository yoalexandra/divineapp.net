from django.conf.urls import include, url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<post_id>\d+)/$',views.posts,name="blog"),
]
