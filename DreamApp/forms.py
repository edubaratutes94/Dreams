from django import forms
from django.forms import *
from DreamApp import models

class SolicitudForm(ModelForm):
    empty_label_message = 'Servicios'

    servicio = ModelChoiceField(
        queryset=models.Service.objects.all(), empty_label=empty_label_message)

    class Meta:
        model = models.Solicitud
        fields = ("servicio","email","full_name","phone","text")



        widgets = {
            'full_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Su Nombre'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Su telefono'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Su mensaje'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Su correo'}),
            'servicio': widgets.Select(attrs={'class': 'form-control required','placeholder':'Servicio'}),
        }
