from django import forms
from .models import *


class FormComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'message', 'email', 'website']

    def __init__(self, *args, **kwargs):
        super(FormComment, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name



