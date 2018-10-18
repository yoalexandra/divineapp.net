from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"),
    url(r'^admin/', admin.site.urls),
]
