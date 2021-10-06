from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


# Create your models here.


class Utilisateur(models.Model):
    CHOIX_PIECES = [('CNI', "Carte Nationale d'Identité"),
                    ('NINA', "NINA"),
                    ('CIC', "Carte d'Identité Consulaire"),
                    ('PASSPORT', "PASSPORT")
                    ]
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
    numid = models.CharField(null=False, blank=False, max_length=50, verbose_name='Identification')
    pieceid = models.CharField(null=False, blank=False, max_length=50, verbose_name='Pièce d\'identité')
    adresse = models.CharField(null=False, blank=False, max_length=250)
    tel = models.CharField(null=False, blank=False, max_length=12)
    photo = models.ImageField(null=True, blank=True, upload_to="photos/", default=None)

    def __str__(self):
        if self.user:
            return f"{self.id}: {self.user.username}"
        return f"{self.id}"


class Projet(models.Model):
    STATUT = [("SDI", "Stade d'Idée"),
              ('EGN', "En Gestation"),
              ('JLC', "Juste Lancé"),
              ('EAE', "En Activité"),
              ('C', "Cloturé")
              ]
    nom = models.CharField(null=False, blank=False, max_length=50, verbose_name='Nom du Projet')
    resume = models.CharField(null=False, blank=False, max_length=250, verbose_name='Description du Projet')
    couverture = models.ImageField(null=True, blank=True, verbose_name="Photo d'Illustration du Projet",
                                   upload_to="photos/")
    secteur = models.CharField(null=False, blank=False, max_length=50, verbose_name="Secteur d'Activité")
    budget = models.FloatField(null=False, blank=False, verbose_name="Budget du Projet")
    statut = models.CharField(null=False, blank=False, max_length=30, choices=STATUT, verbose_name="Statut du Projet")
    date_pub = models.DateTimeField(null=False, blank=False, max_length=30,
                                    verbose_name="Date de Publication du Projet",
                                    default=timezone.now)
    fiche_desc = models.FileField(null=True, blank=True, verbose_name="Fichier de Presentation du Projet")
    user = models.ForeignKey(Utilisateur, null=True, blank=False, on_delete=models.PROTECT)
    donateurs = models.ManyToManyField("Utilisateur", through="deme.Don", related_name="+")
    Investisseurs = models.ManyToManyField("Utilisateur", through="deme.Financement", related_name="+")


class Compte(models.Model):
    rib = models.CharField(null=False, blank=False, max_length=24, verbose_name='Relévé d\'identité banquaire')
    proprietaire = models.ForeignKey(Utilisateur, null=True, blank=False, max_length=50, verbose_name="propriétaire",
                                     on_delete=models.PROTECT)
    nom_banque = models.CharField(null=False, blank=False, max_length=20, verbose_name='Nom de la Banque')
    adresse_banque = models.CharField(null=False, blank=False, max_length=20, verbose_name='Adresse de la banque')
