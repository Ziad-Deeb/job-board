from django import forms
from .models import Job
from django.contrib.auth.forms import UserCreationForm


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location', 'salary', 'application_deadline']

class RegistrationForm(UserCreationForm):
    pass