from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Reaction(models.Model):
	# title = models.CharField(
 #			max_length=200,
 #			validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
 #	)
	text = text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	responses = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Response', related_name='thread_responses')

	# r = len(Response.objects.all().filter(reaction=self.id))

	# def get_num_responses(self):
	# 	r = Response.objects.all().filter(reaction=self.id)
	# 	return len(r)

	def __str__(self):
		return self.text

class Response(models.Model):
	text = text = models.TextField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

	def __str__(self):
		return self.text
