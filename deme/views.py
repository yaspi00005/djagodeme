from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from djago.models import Utilisateur
from .forms import CreationDon, CreationFinance

# Create your views here.


def liste_tous_dons(request):
    from .models import Don
    dons = Don.objects.filter(utilisateur__user=request.user)
    return render(request, 'deme/listeDon.html', locals())


def liste_financement(request):
    from .models import Don
    dons = Don.objects.filter(utilisateur__user=request.user)
    return render(request, 'deme/listeFinancement.html', locals())

# @login_required(login_url="don")


def FaireDon(request):
    form = CreationDon(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect(liste_tous_dons,)
    return render(request, "deme/don.html", locals())


def financer(request):
    form = CreationFinance(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect(liste_tous_dons,)
    return render(request, "deme/financement.html", locals())


def lister_don(request):
    return render(request, "deme/financement.html", locals())
