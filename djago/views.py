from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ConnectForm
from .forms import CreerProjetForm
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm
from django.contrib.auth import logout

# Create your views here.


def accueil(request):
    # user = request.GET.get('u', '')
    # if user != '':
    #     return HttpResponse(f"<h1>Bonjour {user}. Bienvenu sur Djago dèmè.")
    # else:
    #     return HttpResponse("<h1>Bonjour, bienvenu sur Djago dèmè</h1>")
    user = request.user
    return render(request, "djago/accueil.html", locals())


def inscription(request):
    form = InscriptionForm(request.POST or None)
    form.fields['username'].widget.attrs = {'class': 'form-control'}
    form.fields['email'].widget.attrs = {'class': 'form-control'}
    form.fields['password1'].widget.attrs = {'class': 'form-control'}
    form.fields['password2'].widget.attrs = {'class': 'form-control'}
    if form.is_valid():
        user = form.save(commit=False)
        from .models import Utilisateur
        utilisateur = Utilisateur(user=user)
        user.save()
        utilisateur.save()
        erreur = False
    else:
        erreur = True
    return render(request, "djago/inscription.html", locals())


def deconnexion(request):
    if (request.user):
        logout(request)
    return redirect(accueil)


def connexion(request):
    form = ConnectForm(request.POST or None)
    erreur = False
    if form.is_valid():
        username = form.cleaned_data["login"]
        password = form.cleaned_data["m_pass"]
        from django.contrib.auth import authenticate, login
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(lister_projets, budget=0, statut='SDI')
        else:
            erreur = True
    return render(request, "djago/connexion.html", locals())


def chercher_projet(request, id_projet):
    from django.db import models
    from .models import Projet
    try:
        ligne = Projet.objects.get(id=id_projet)
        return render(request, 'djago/chercher_projet.html', {'find':1, 'ligne':ligne})
    except models.ObjectDoesNotExist:
        return render(request, 'djago/chercher_projet.html', {'find':0, 'id_projet':id_projet})

def lister_projets(request, budget, statut='C'):
    from django.http import Http404
    if statut not in ["SDI", 'EGN', 'JLC', 'EAE', 'C']:
        raise Http404
    else:
        from .models import Projet
        projets = Projet.objects.filter(budget__gte=budget, statut=statut)
        return render(request, 'djago/lister_projets.html', locals())

def liste_tous_projets(request):
    from .models import Projet
    projets = Projet.objects.all()
    return render(request, 'djago/listeTousProjets.html', locals())

@login_required(login_url="accueil")
def creerProjet(request):
    form = CreerProjetForm(request.POST or None)
    if form.is_valid():
        form.user = request.user
        form.save()
        return redirect(lister_projets, budget=0, statut='SDI')
    return render(request, "djago/creationProjet.html", locals())