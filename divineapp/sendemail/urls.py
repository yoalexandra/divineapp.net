# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.conf.urls import include, url
from divineapp.sendemail import views as sendemail_views

urlpatterns = [
    url(r'^$',sendemail_views.index, name="index"),
    url(r'^sendemail/thankyou$',TemplateView.as_view(template_name='sendemail/thankyou.html'),name="send_email_thankyou"),
]
