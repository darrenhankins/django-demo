# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def new(request):
    return HttpResponse("Hello, world. This is a new poll!!!!")

def list(request):
    return HttpResponse("Hello, world. This is a list of polls...")
