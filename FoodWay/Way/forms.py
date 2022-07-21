from django import forms

from .models import PagePlace

class PagePlaceForm(forms.ModelForm):
    class Meta:
        model = PagePlace
        fields = '__all__'

class name_of_Way(forms.Form):
    name_way = forms.CharField(max_length=150,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Название вашего Way'}))

 