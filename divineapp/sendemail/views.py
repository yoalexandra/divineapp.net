# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.mail import EmailMessage
from .forms import ContactForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # redirect to a new URL:
            return HttpResponseRedirect('thank_you')
    else:
        form = ContactForm(label_suffix=' : ',initial={'user':request.user,'otherstuff':'otherstuff'},use_required_attribute=False,auto_id=False)
    return render(request,'sendemail/index.html',{'form':form })

def thank_you(request):
    return render(request, 'sendemail/thankyou.html')


"""
 field_order=['email','name','comment']

 
 """
