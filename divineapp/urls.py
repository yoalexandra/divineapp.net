from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

#from divineapp.home import views as home_views
from divineapp.blog import views as blog_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^home/', home_views.contacts),
    url(r'^home/', include('divineapp.home.urls',namespace="home")),
    url(r'^blog/', blog_views.posts),
    url(r'^blog/(?P<post_id>\d+)/',blog_views.posts),
]
