from django import forms

from .models import Users

class CsForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = [
			'name',
			'email'
		]