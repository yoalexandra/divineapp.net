from django.conf.urls import include, url
from divineapp.blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    url(r'^$',blog_views.index,name="index"),
]
