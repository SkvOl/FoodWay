from dataclasses import fields
from django import forms
from .models import PagePlaces, Feedback
from ckeditor_uploader.fields import RichTextUploadingFormField

class PagePlacesForm(forms.ModelForm):
    name = forms.CharField(label='name PagePlaces', min_length=5, max_length=150,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Название (от 5 до 150 символов)'}))

    content = RichTextUploadingFormField()

    short_info = forms.CharField(label='short informaton', max_length = 200,
                                 widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Краткая информация (до 200 символов)'}))

    url = forms.CharField(label='custom url', max_length = 20,
                          widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Сделайте выделяющийся адрес (до 20 символов)'}))

    #icon = forms.FileField(widget=forms.FileInput({
    #                               'class': 'form-control',
    #                               'placeholder': 'По желанию, загрузите иконку'}),required=False)

    class Meta:
        model = PagePlaces
        fields = ['name', 'content', 'short_info', 'url', 'icon_id', 'lat', 'lng']


class FeedbackForm(forms.ModelForm):

    rating = forms.IntegerField(label = 'Рейтинг', max_value = 5, min_value=0, initial=1)
    content = forms.CharField(label = 'Текст комментария', max_length = 1000, 
                             widget=forms.Textarea({
                                    'class':'form-control','rows':'3','placeholder':'Ваш комментарий'}), required=False)

    class Meta:
        model = Feedback
        fields = ['rating','content']


