from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^contacts/$',views.contacts,name="contacts"),
]
