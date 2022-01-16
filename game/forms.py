from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    class Meta:
        model= User
        fields=[
            'username'
        ]
    

