from django import forms


class name_of_Way(forms.Form):
    name_way = forms.CharField(max_length=150,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Название вашего Way'}))

 