from django import forms

from django.urls import reverse
from crispy_forms.helper import FormHelper

from threads.models import Reaction, Response, Brainstorm, BrainstormResponse, BrainstormComment, Discussion, DiscussionReply
class ResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ['text', 'owner']  # Picture is manual
	#resp = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
	#owner = User

class BrainResponseForm(forms.ModelForm):
	class Meta:
		model = BrainstormResponse
		fields = ['text', 'owner']

class BrainCommentForm(forms.ModelForm):
	class Meta: 
		model = BrainstormComment
		fields = ['text', 'owner']


class ReplyForm(forms.ModelForm):
	class Meta:
		model = Discussion
		fields = ['text', 'owner']


class ReactForm(forms.ModelForm):
	class Meta:
		model = Reaction
		fields = ['topic','text', 'owner']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		form.helper.form_action = reverse('threads:reaction_detail', kwargs={'react_id': react.id})
