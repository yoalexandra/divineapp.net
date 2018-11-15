# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import ContactForm


def index(request):
    form = ContactForm()
    return render(request,'sendemail/index.html',{'form':form })
