from django import forms
from django.forms import widgets
from .models import SignUpEmail, SignUpInfo
import re

class SignUpForm(forms.ModelForm):
	email = forms.EmailField(required=True, max_length=80, widget=widgets.TextInput(attrs={'placeholder': 'Email Address',
																						   'class':'subscribe-input to-center'}))

	class Meta:
		model = SignUpEmail
		fields = ('email',)

class SignUpInfoForm(forms.ModelForm):
	first_name = forms.CharField(required=True, max_length=30, widget=widgets.TextInput(attrs={'placeholder':'First Name'}))
	last_name = forms.CharField(required=True, max_length=30, widget=widgets.TextInput(attrs={'placeholder':'Last Name'}))
	phone = forms.CharField(required=True, max_length=20, widget=widgets.TextInput(attrs={'placeholder':'Phone Number'}))

	def clean_phone(self):
		phone = self.cleaned_data.get('phone', False)
		if phone:
			phone_regex = re.compile(r"^[0-9]+")
			if not phone_regex.match(phone):
				raise ValidationError("Not a valid phone number")
			return phone
		else:
			raise ValidationError("Phone Number is required")


	class Meta:
		model = SignUpInfo
		fields = ('first_name', 'last_name', 'phone')