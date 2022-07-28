
from django import forms
from django.forms import ModelForm
from django.forms.fields import EmailField 
from .models import User_info


class User_info_form(forms.Form):
    first_name = forms.CharField(max_length=150,
                               widget=forms.TextInput({
                                   'class': 'form-control'}))

    last_name = forms.CharField(max_length=150,
                               widget=forms.TextInput({
                                   'class': 'form-control'}))


    phone = forms.CharField(required=False, max_length=13,
                               widget=forms.TextInput({
                                   'class': 'form-control'}))

    show_phone = forms.BooleanField(required=False)

    url_user = forms.CharField(max_length=30,
                                widget=forms.TextInput({
                                   'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput({
                                   'class': 'form-control'}), required=False)

    show_email = forms.BooleanField(required=False)

    image_profile = forms.ImageField(required=False)

    about_user = forms.CharField(max_length=2000, widget=forms.Textarea({
                                    'class':'form-control','rows':'3'}), required=False)


#class Profile_info_form(forms.ModelForm):
#    class Meta:
#        model = User_info
#        fields = ('first_name','phone','show_phone','url_user','show_email','about_user')
#        widgets = {
            
#            }
    
 