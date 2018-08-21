from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
	user = models.ForeignKey(User, on_delete='CASCADE')
	title = models.CharField(max_length=250)
	body = models.TextField()
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		blog_entry = self.title + "\n" + self.body
		return blog_entry


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete='CASCADE')
	blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	body = models.TextField()
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		comment_entry = self.blogpost.title + "\n" + self.body
		return comment_entry
