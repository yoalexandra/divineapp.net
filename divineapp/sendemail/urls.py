# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^thank_you/$', views.thank_you, name="thank_you")
]
