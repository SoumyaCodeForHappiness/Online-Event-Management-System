from django import forms
from django.forms import fields

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')