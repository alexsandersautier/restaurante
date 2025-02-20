from django import forms
from django.contrib.auth.models import User

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user'}),
            'password': forms.PasswordInput(attrs={'class': 'password'})
        }