from django import forms
from .models import Event, Person, Cause,work

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date picker
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name', 'photo', 'phone', 'email', 'address', 
            'disability_type', 'dis_percentage', 'udid_no', 
            'aadhaar_no', 'age', 'gender', 'dependent', 
            'occupation', 'salary', 'it_return'
        ]
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'disability_type': forms.TextInput(attrs={'class': 'form-control'}),
            'dis_percentage': forms.TextInput(attrs={'class': 'form-control'}),
            'udid_no': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhaar_no': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'dependent': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'it_return': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CauseForm(forms.ModelForm):
    class Meta:
        model = Cause
        fields = ['name', 'img', 'detail', 'raised', 'goal']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'raised': forms.NumberInput(attrs={'class': 'form-control'}),
            'goal': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class WorkForm(forms.ModelForm):
    class Meta:
        model = work
        fields = ['name', 'img', 'detail']