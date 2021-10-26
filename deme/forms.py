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


class DonProjet(forms.Form):
    utilisateur = forms.CharField(label="Utilisateur", max_length=40, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
    projet = forms.CharField(label="Projet", max_length=40, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
    montant = forms.IntegerField(label="Montant",  widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Montant du don"}))


class FinanceProjet(forms.Form):
    class Meta:
        model = Financement
        utilisateur = forms.CharField(label="Utilisateur", max_length=40, disabled=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
        projet = forms.CharField(label="Projet", max_length=40, disabled=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
        montant = forms.IntegerField(label="Montant",  widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
        duree = forms.IntegerField(label="Duée",  widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
        date_debut = forms.IntegerField(label="Date",  widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Montant du don"}))
