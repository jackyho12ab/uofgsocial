# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class College(models.Model):
	name = models.CharField(max_length=255)

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

class Follow(models.Model):
	user = models.ForeignKey(User)
	module = models.ForeignKey(Module)

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