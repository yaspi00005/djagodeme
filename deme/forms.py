from django import forms
from django.forms.models import ModelChoiceField, ModelForm
from django.http import request
from .models import Don, Financement
from djago.models import Projet


class CreationDon(ModelForm):
    class Meta:
        model = Don
        exclude = ['utilisateur']

    # Projet = forms.CharField(max_length=30)
    # utilisateur = forms.CharField(max_length=30, disabled=True)
    # Montant = forms.FloatField(required=True)


class CreationFinance(ModelForm):
    class Meta:
        model = Financement
        exclude = ['utilisateur']


class DonProjet(forms.Form):
    utilisateur = forms.CharField(label="Utilisateur", max_length=40, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
    projet = forms.CharField(label="Projet", max_length=40, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
    montant = forms.IntegerField(label="Montant",  widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
