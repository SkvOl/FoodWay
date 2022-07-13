"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError 
from django.forms.fields import EmailField 
from django.forms.forms import Form 


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

    
class CustomUserCreationForm(UserCreationForm): 
    username = forms.CharField(label='username', min_length=5, max_length=150, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'})) 

    email = forms.EmailField(label='email',widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder':'Email'}))
    
    password1 = forms.CharField(label='password', min_length=8, widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
    
    password2 = forms.CharField(label='Confirm password', min_length=8, widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Подтвердите пароль'})) 
 