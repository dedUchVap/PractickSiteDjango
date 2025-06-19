from apps.core.models import *
from django import forms
class ApplicationForm(forms.ModelForm):
    project_name = forms.TextInput()
    class Meta:
        model = Application
        fields = ['project_name', 'description', 'address']
        labels = {
            'project_name': 'Название проекта',
            'description': 'Описание работ',
            'address': 'Адрес объекта',
        }
