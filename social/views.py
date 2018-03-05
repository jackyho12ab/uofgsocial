# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'pages/index.html')
    return response

def content(request):
    reponse = render(request, 'pages/content.html')
    return reponse

def editprofile(request):
    reponse = render(request, 'pages/editprofile.html')
    return reponse

def viewprofile(request):
    reponse = render(request, 'pages/viewprofile.html')
    return reponse

def login(request):
    reponse = render(request, 'pages/login.html')
    return reponse

def register(request):
    reponse = render(request, 'pages/register.html')
    return reponse
