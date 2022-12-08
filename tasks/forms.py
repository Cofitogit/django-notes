from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        labels = {
            'title': _('Titulo'),
            'description': _('Descripción'),
            'important': _('¿Es esta tarea de caracter importante?  '),
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo', 'style': 'background: rgb(32, 27, 32); color: white;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la descripción', 'style': 'background: rgb(32, 27, 32); color: white;'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input col-sm-6 float-end'}),
        }

        