from django import forms

from django.urls import reverse
from crispy_forms.helper import FormHelper

from threads.models import Reaction, Response, Brainstorm, BrainstormResponse, BrainstormComment, Discussion, DiscussionReply

class ReactForm(forms.ModelForm):
	class Meta:
		model = Reaction
		fields = ['topic','text']

class ResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ['text']
	#resp = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
	#owner = User

#-----------------------------------------------------------------------------

class BrainForm(forms.ModelForm):
	class Meta:
		model = Brainstorm
		fields = ['topic', 'text']  # Picture is manual

class BrainResponseForm(forms.ModelForm):
	class Meta:
		model = BrainstormResponse
		fields = ['text']

class BrainCommentForm(forms.ModelForm):
	class Meta: 
		model = BrainstormComment
		fields = ['text']

#-----------------------------------------------------------------------------

class DiscForm(forms.ModelForm):
	class Meta:
		model = Discussion
		fields = ['topic','text']

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Discussion
		fields = ['text']
	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.helper = FormHelper()
	# 	form.helper.form_action = reverse('threads:reaction_detail', kwargs={'react_id': react.id})
