# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from social.models import Post, Comment, UserProfile, University
from django.contrib.auth import authenticate, login
from social.forms import UserForm, UserProfileForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpReponse("Your account is disabled.")
        else:

            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpReponse("Invalid login details")

    else:

        return render(request, 'pages/login.html', {})


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
        
            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'pages/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})





@login_required
def user_logout(request):
    
    logout(request)
    return HttpResponseRedirect(reverse('index'))

