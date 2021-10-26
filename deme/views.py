from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from deme.models import Financement

from djago.models import Utilisateur
from djago.views import liste_tous_projets
from .forms import CreationDon, CreationFinance, DonProjet, FinanceProjet


# Create your views here.

@login_required(login_url="accueil")
def liste_tous_dons(request):
    from .models import Don
    dons = Don.objects.filter(utilisateur__user=request.user)
    return render(request, 'deme/listeDon.html', locals())


@login_required(login_url="accueil")
def FaireDon(request):
    form = CreationDon(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(liste_tous_dons, )
    return render(request, "deme/don.html", locals())


@login_required(login_url="accueil")
def financer(request):
    form = CreationFinance(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(liste_tous_dons, )
    return render(request, "deme/financement.html", locals())


@login_required(login_url="accueil")
def FaireDonProjet(request, id_projet):
    # print(id_projet)
    form = DonProjet(request.POST or None)
    id_projet = id_projet
    from djago.models import Utilisateur
    from djago.models import Projet
    from .models import Don
    user = request.user
    utilisateur = Utilisateur.objects.get(user=request.user)
    projet = Projet.objects.get(id=id_projet)
    don = Don()
    # print(request.user.username)
    form.fields["utilisateur"].initial = f" {request.user.username}: {request.user.first_name} {request.user.last_name} "
    form.fields["projet"].initial = projet.nom + \
        " (" + projet.statut + ") secteur: " + projet.secteur
    if form.is_valid():
        don.projet = projet
        don.utilisateur = utilisateur
        don.montant = form.cleaned_data["montant"]
        don.save()
        return redirect(liste_tous_projets)

    return render(request, 'deme/donate.html', locals())
    # return HttpResponse(f"<h2>un pari {id_projet}</h2>")


@login_required(login_url="accueil")
def financerprojet(request, id_projet):
    # print(id_projet)
    form = DonProjet(request.POST or None)
    idpro = id_projet
    from djago.models import Utilisateur
    from djago.models import Projet
    from .models import Don
    user = request.user
    utilisateur = Utilisateur.objects.get(user=request.user)
    projet = Projet.objects.get(id=idpro)
    financer = Financement()
    # print(request.user.username)
    form.fields["utilisateur"].initial = f" {request.user.username}: {request.user.first_name} {request.user.last_name} "
    form.fields["projet"].initial = projet.nom + \
        " (" + projet.statut + ") secteur: " + \
        projet.secteur
    form.fields["montant"].initial = str(projet.budget)
    if form.is_valid():
        financer.projet = projet
        financer.utilisateur = utilisateur
        financer.montant = form.cleaned_data["montant"]
        financer.save()
        return redirect(liste_tous_projets)

    return render(request, 'deme/financer.html', locals())
    # return HttpResponse(f"<h2>un pari {id_projet}</h2>")


@login_required(login_url="accueil")
def donliste(request, id_projet):
    # print(id_projet)
    form = DonProjet(request.POST or None)
    idpro = id_projet
    from djago.models import Utilisateur
    from djago.models import Projet
    from .models import Don
    user = request.user
    utilisateur = Utilisateur.objects.get(user=request.user)
    dons = Don.objects.filter(projet=idpro)
    s = 0
    count = dons.count()

    financer = Financement()
    # print(request.user.username)

    return render(request, 'deme/listeDon.html', locals())
    # return HttpResponse(f"<h2>un pari {id_projet}</h2>")


def liste_financement(request, id_projet):
    # print(id_projet)
    form = FinanceProjet(request.POST or None)
    idpro = id_projet
    from djago.models import Utilisateur
    from djago.models import Projet
    from .models import Don
    user = request.user
    utilisateur = Utilisateur.objects.get(user=request.user)
    dons = Financement.objects.filter(projet=idpro)
    s = 0
    count = dons.count()

    financer = Financement()
    # print(request.user.username)

    return render(request, 'deme/listeDon.html', locals())
    # return HttpResponse(f"<h2>un pari {id_projet}</h2>")
