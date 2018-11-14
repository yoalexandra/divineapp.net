# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import ContactForm


def index(request):
    return render(request,'sendemail/index.html')

def send_email(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # process data, insert into DB, generate email,etc
            # redirect to a new URL:
            return HttpResponseRedirect('/sendemail/send_email/thankyou')
    else:
        # GET, generate blank form
        form = ContactForm(label_suffix=' : ',initial={'user':request.user,'otherstuff':'otherstuff'},use_required_attribute=False,auto_id=False)
    return render(request,'sendemail/send_email.html',{'form':form})
