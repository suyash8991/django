from django import forms
from .models import User,Register
class signup(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
    class Meta():
        model=User
        fields=('first_name','last_name','email','username','password')
        help_texts = {
            'username': None,
            'email': None,
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'inputstyle'}),
            'last_name':forms.TextInput(attrs={'class':'inputstyle'}),
            'email':forms.EmailInput(attrs={'class':'inputstyle'}),
            'username':forms.TextInput(attrs={'class':'inputstyle'}),
        }
class regform(forms.ModelForm):
    class Meta:
        model=Register
        fields=('phone_number',)
        widgets={
            'phone_number':forms.TextInput(attrs={'class':'inputstyle'})
        }
class loginformm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'inputstyle'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputstyle'}))
