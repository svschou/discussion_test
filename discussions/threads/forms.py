from django import forms
from threads.models import Reaction, Response
class ResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ['text', 'owner']  # Picture is manual
	#resp = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
	#owner = User