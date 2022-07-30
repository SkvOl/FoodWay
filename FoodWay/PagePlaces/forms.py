from django import forms
from .models import PagePlaces
from ckeditor_uploader.fields import RichTextUploadingFormField

class PagePlacesForm(forms.ModelForm):
    name = forms.CharField(label='name PagePlaces', min_length=5, max_length=150,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Название'}))

    content = RichTextUploadingFormField()

    short_info = forms.CharField(label='short informaton', max_length = 200,
                                 widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Краткая информация'}))

    url = forms.CharField(label='custom url', max_length = 20,
                          widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Сделать выделяющийся url'}))

    class Meta:
        model = PagePlaces
        fields = ['name', 'content', 'short_info', 'url']


