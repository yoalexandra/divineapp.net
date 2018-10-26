from django.conf.urls import include, url
from divineapp.apps import views as apps_views

urlpatterns = [
    url(r'^$',apps_views.index,name="index"),
    url(r'^(?P<app_id>\d+)/$',apps_views.apps,name="apps"),

]
