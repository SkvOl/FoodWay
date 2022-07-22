
from django import forms
from django.forms import ModelForm
from django.forms.fields import EmailField 


class FormProfile(forms.Form):
    firstname = forms.CharField(max_length=150,
                               widget=forms.TextInput({
                                   'class': 'form-control'}))

    phone = forms.CharField(max_length=13,
                               widget=forms.TextInput({
                                   'class': 'form-control'}))

    show_phone = forms.BooleanField()

    url_user = forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                   'class': 'form-control'}))

    email = forms.EmailField(label='email',widget=forms.EmailInput({
                                   'class': 'form-control'}))

    show_email = forms.BooleanField()

    #about_user = forms.TextField()
    
 