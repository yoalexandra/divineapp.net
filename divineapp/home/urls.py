from django.conf.urls import include, url
from divineapp.home import views as home_views

urlpatterns = [
    url(r'^$',home_views.index,name="index"),
    url(r'^contacts/$',home_views.contacts,name="contacts"),
]
