from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Reaction(models.Model):
	topic = models.TextField(default='General')
	text = text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	responses = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Response', related_name='thread_responses')

	def __str__(self):
		return self.topic

class Response(models.Model):
	text = text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)
	reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

# ----------------------------------------------------------------------------

class Brainstorm(models.Model):
	topic = models.TextField(default='General')
	text = text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	brainstormresponses = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BrainstormResponse', related_name='thread_brainstormresponses')

	def __str__(self):
		return self.topic

class BrainstormResponse(models.Model):
	text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	brainstorm = models.ForeignKey(Brainstorm, on_delete=models.CASCADE)
	# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/self_fk.html
	#parent = models.ForeignKey("self", on_delete=models.CASCADE) # making this optional
	#level = 1

	votes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Vote', related_name='thread_brainstormresponsevotes')
	comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BrainstormComment', related_name='thread_brainstormresponsecomments')

	def __str__(self):
		return self.text

class BrainstormComment(models.Model): # ask Chuck?
	text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	brainstormresponse = models.ForeignKey(BrainstormResponse, on_delete=models.CASCADE)
	#parent = models.ForeignKey(BrainstormResponse, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

class Vote(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	brainresponse = models.ForeignKey(BrainstormResponse, on_delete=models.CASCADE)
	#direction = mdoels.IntegerField(default=1)
	vote_choices = [('u','UP'), ('d','DOWN')]
	direction = models.CharField(max_length=1, choices=vote_choices, default=vote_choices[0][0])

	def __str__(self):
		return self.brainresponse.text

# ----------------------------------------------------------------------------

class Discussion(models.Model):
	topic = models.TextField(default='General')
	text = models.TextField(default='What do you think?')
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	replies = models.ManyToManyField(settings.AUTH_USER_MODEL, through='DiscussionReply', related_name='thread_replies')

	def __str__(self):
		return self.topic

class DiscussionReply(models.Model):
	text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)

	discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

	def __str__(self):
		return self.text



