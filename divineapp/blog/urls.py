from django.conf.urls import include, url
from divineapp.blog import views as blog_views

urlpatterns = [
    url(r'^blog/',blog_views.posts),
    url(r'^blog/(?P<post_id>\d+)/',blog_views.posts),
]
