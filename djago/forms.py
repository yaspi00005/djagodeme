from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Projet


class ConnectForm(forms.Form):
    login = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    m_pass = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))


class CreerProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        nom = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nom du projet'}))
        resume = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        exclude = ("user", "donateurs", "Investisseurs")


class InscriptionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        username = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'yaya'}))
        email = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'yaya'}))
        password1 = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'yaya'}))
        password2 = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'yaya'}))


class ProfilForm(forms.Form):
    login = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    email = forms.EmailField(label='Email', max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    numid = forms.CharField(label="Numéro d'identification", max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Numéro d'identification"}))
    pieceid = forms.CharField(label="Pièce d'identité", max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Pièce d'identité"}))
    adresse = forms.CharField(label="Adresse", max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Adresse"}))
    tel = forms.CharField(label="Téléphone", max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Téléphone"}))
    photo = forms.ImageField(label="Photo")
