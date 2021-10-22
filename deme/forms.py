from django import forms
from django.forms.models import ModelChoiceField, ModelForm
from django.http import request
from .models import Don, Financement
from djago.models import Projet


class CreationDon(ModelForm):
    class Meta:
        model = Don
        exclude = ['utilisateur']

        projet = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        widgets = {
            "montant": forms.TextInput(attrs={'placeholder': 'Montant', 'class': 'form-control'}),
        }


class CreationFinance(ModelForm):
    class Meta:
        model = Financement
        exclude = ['utilisateur']
