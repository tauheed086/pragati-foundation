# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Agent

class AgentSignupForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = ['username', 'email', 'password1', 'password2']
