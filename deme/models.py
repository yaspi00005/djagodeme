from django.db import models

# Create your models here.


class Don(models.Model):
    montant = models.FloatField(null=False, blank=False, max_length=10)
    utilisateur = models.ForeignKey('djago.Utilisateur', null=True, blank=False, on_delete=models.PROTECT)
    projet = models.ForeignKey('djago.Projet', null=True, blank=False, on_delete=models.PROTECT)


class Versement(models.Model):
    ref = models.CharField(null=False, blank=False, max_length=50, verbose_name='Référence')
    date = models.DateTimeField(null=False, blank=False, max_length=30)
    don = models.OneToOneField('Don', on_delete=models.SET_NULL, null=True, blank=False)
    financement = models.ForeignKey('Financement', related_name="+", on_delete=models.SET_NULL,null=True)
    source = models.ForeignKey('djago.Compte',verbose_name="source", related_name="Versements_effectués",on_delete=models.SET_NULL, null=True, blank=False,default=None,)
    destination = models.ForeignKey('djago.Compte',verbose_name="destination", related_name="Versements_reçus",on_delete=models.SET_NULL, null=True, blank=False,default=None)


class Financement(models.Model):
    date_debut = models.DateField(null=False, blank=False, verbose_name="Date de début")
    duree = models.IntegerField(null=False, blank=False, max_length=6, verbose_name='Durée')
    montant = models.FloatField(null=False, blank=False, max_length=10)
    utilisateur = models.ForeignKey('djago.Utilisateur', null=True, blank=False, on_delete=models.PROTECT)
    projet = models.ForeignKey('djago.Projet', null=True, blank=False, on_delete=models.PROTECT)