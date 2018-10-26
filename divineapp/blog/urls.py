from django.conf.urls import include, url
from divineapp.blog import views as blog_views

urlpatterns = [
    url(r'^$',blog_views.index,name="index"),
    url(r'^(?P<post_id>\d+)/$',blog_views.posts,name="blog"),

]
