from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','department','contact_no','profile_pic','role']
    password = forms.CharField(widget=forms.PasswordInput())
