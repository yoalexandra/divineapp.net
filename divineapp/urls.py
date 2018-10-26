from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"),
    url(r'^blog/',include('divineapp.blog.urls',namespace="blog")),
    url(r'^apps/',include('divineapp.apps.urls',namespace="apps")),
    url(r'^home/', include('divineapp.home.urls',namespace="home")),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]
