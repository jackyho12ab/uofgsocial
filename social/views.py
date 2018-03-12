# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from social.models import Post, Comment, UserProfile, University

from django.shortcuts import render

# Create your views here.
def index(request):
    university_list = University.objects
    context_dict = { 'PageTitle' : 'UofGSocial',
                    'Universities' : university_list}
    response = render(request, 'pages/index.html', context_dict)
    return response

def content(request):
    post_list = Post.objects
    comment_list = Comment.objects
    user_list = UserProfile.objects
    context_dict = { 'PageTitle' : 'Recent Posts',
                    'Users' : user_list,
                    'Posts' : post_list,
                    'Comments' : comment_list}
    reponse = render(request, 'pages/content.html', context_dict)
    return reponse

def editprofile(request):
    post_list = Post.objects
    comment_list = Comment.objects
    user_list = UserProfile.objects
    context_dict = { 'PageTitle' : 'Edit Profile',
                    'Users' : user_list,
                    'Posts' : post_list,
                    'Comments' : comment_list}
    reponse = render(request, 'pages/editprofile.html', context_dict)
    return reponse

def viewprofile(request):
    post_list = Post.objects
    comment_list = Comment.objects
    user_list = UserProfile.objects
    context_dict = { 'PageTitle' : 'View Profile'}
    reponse = render(request, 'pages/viewprofile.html', context_dict)
    return reponse

def login(request):
    context_dict = { 'PageTitle' : 'Login'}
    reponse = render(request, 'pages/login.html', context_dict)
    return reponse

def register(request):
    context_dict = { 'PageTitle' : 'Register'}
    reponse = render(request, 'pages/register.html', context_dict)
    return reponse
