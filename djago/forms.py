from django import forms
from .models import Projet

class ConnectForm(forms.Form):
    login = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nom d\'utilisateur'}))
    m_pass = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Mot de passe'}))


class CreerProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        exclude = ("user", "donateurs", "Investisseurs")


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class InscriptionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yaya'}))
        email = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yaya'}))
        password1 = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yaya'}))
        password2 = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'yaya'}))

