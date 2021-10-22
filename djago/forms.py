from string import Template

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.safestring import mark_safe

from .models import Projet


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        # html =
        html = Template("""
        <img src="media/$link" width="100" height=120/><br><br>
        <input type="file" name="photo" accept="image/*" id="id_photo"><br><br>""")
        return mark_safe(html.substitute(link=value))


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
        secteur = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        budget = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        statut = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        date_pub = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        couverture = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        user = forms.CharField(max_length=30, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Resume'}))
        exclude = ("donateurs", "Investisseurs")


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
        attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}))
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


class ProfilImageForm(forms.Form):
    photo = forms.ImageField(label="Photo")