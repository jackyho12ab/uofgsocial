# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
	name = models.CharField(max_length=255)
	logo = models.ImageField(blank=True)
	colour = models.CharField(max_length=6)
	email_domain = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class College(models.Model):
	name = models.CharField(max_length=255)
	university = models.ForeignKey(University)

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=255)
	college = models.ForeignKey(College)

	def __str__(self):
		return self.name

class Module(models.Model):
	name = models.CharField(max_length=255)
	subject = models.ForeignKey(Subject)

	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(blank=True)
	location = models.CharField(blank=True, max_length=255)
	bio = models.TextField(blank=True)
	dob = models.DateField(blank=True)
	university = models.ForeignKey(University)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name + " (" + self.university + " )"

class Follow(models.Model):
	user = models.ForeignKey(User)
	module = models.ForeignKey(Module)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name + " follows " + self.module

class Post(models.Model):
	content = models.TextField()
	image = models.ImageField(blank=True)
	video = models.URLField(blank=True)
	likes = models.IntegerField(default=0)
	module = models.ForeignKey(Module)
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	content = models.TextField()
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User)
	link = models.URLField()
	read = models.BooleanField()