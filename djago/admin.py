from django.contrib import admin, messages

# Register your models here.
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext

from .models import *
from deme.admin import VersementInlineSource, VersementInlineDest

admin.site.site_header = "Djago dèmè"
admin.site.site_title = "Djago dèmè"
admin.site.index_title = "Tableau de bord"



class ProjetInline(admin.TabularInline):
    model = Projet
    fk_name = 'user'
    fields = ('id', 'nom', 'secteur', 'budget', 'statut')
    extra = 0
    classes = ['collapse']


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'numid', 'pieceid', 'adresse', 'tel']
    list_filter = ['pieceid', 'adresse']
    # date_hierarchy = ('user__date_joined',)
    ordering = ['user__first_name', 'user__last_name', 'user__username']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'numid', 'tel']
    fieldsets = [
        ("Informations personnelles", {
            "classes": ["collapse", "start-open"],
            "fields": ("user", "photo_image", "photo", "numid", "pieceid")}),
        ("Contacts", {
            "description": 'Text indicatif',
            "classes": ["collapse", "start-open"],
            'fields': ('adresse', 'tel')})
    ]
    inlines = [ProjetInline]
    autocomplete_fields = ['user', ]
    readonly_fields = ['photo_image', ]

    def photo_image(self, obj):
        if obj.photo:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.photo.url,
                    width=80,
                    height=100,
                )
            )
        return None


@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
     list_display = ['id', 'rib', 'proprietaire', 'nom_banque', 'adresse_banque']
     list_filter = ['nom_banque', 'proprietaire']
     ordering = ['proprietaire__user__first_name', 'proprietaire__user__last_name', 'nom_banque']
     search_fields = ['rib', 'proprietaire__user__first_name', 'proprietaire__user__last_name']
     fieldsets = [
        ("Informations du titulaire",{
             "classes": [],
            "fields":("proprietaire",)}),
         ("Informations sur le Compte", {
            #'description':'Ce compte a un proprietaire du nom de:',
             "classes": ["collapse", "start-open"],
            "fields":("rib", "nom_banque", 'adresse_banque')
         })
         ]
     autocomplete_fields = ['proprietaire',]
     inlines = [VersementInlineSource, VersementInlineDest]


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'resume', 'secteur', 'budget', 'statut', 'date_pub', 'user']
    list_filter = ['secteur', 'statut']
    date_hierarchy = 'date_pub'
    search_fields = ['nom']
    ordering = ['date_pub', 'nom', '-budget']
    fieldsets = [
        ("Sommaire du projet", {
            "classes": [],
            "fields": ("user", "nom", "resume", "budget", "date_pub")}),
        ("Détails du projet", {
            "classes": ["collapse", "start-open"],
            "fields": ("couverture_image", "couverture", "secteur", 'statut', "fiche_desc")
        }),
        ("Aide du projet", {
            "classes": ["collapse", "start-open"],
            "fields": ("nombre_dons", "total_dons", 'donateurs', "nombre_financements", "total_financements", 'Investisseurs')
        })
    ]
    autocomplete_fields = ['user', ]
    readonly_fields = ['date_pub', 'couverture_image', 'nombre_dons', "total_dons", "nombre_financements", "total_financements", "donateurs", 'Investisseurs']
    filter_horizontal = ['donateurs', 'Investisseurs']
    save_on_top = True
    actions = ['cloturer_projet']

    change_form_template = "djago/classe_change_form.html"

    def couverture_image(self, obj):
        if obj.couverture:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.couverture.url,
                    width=obj.couverture.width/4,
                    height=obj.couverture.height/4,
                )
            )
        return None

    def nombre_dons(self, obj):
        # return len(obj.donateurs.all())
        return obj.donateurs.all().count()

    def total_dons(self, obj):
        s = 0
        for don in obj.donateurs.all():
            s += don.montant
        return f"{s} F"

    def nombre_financements(self, obj):
        # return len(obj.Investisseurs.all())
        return obj.Investisseurs.all().count()

    def total_financements(self, obj):
        s = 0
        for inv in obj.Investisseurs.all():
            s += inv.montant
        return f"{s} F"

    # Elle permet de définir une action (cloturer) sur un lot de projets sélectionnés dans la liste (display).
    def cloturer_projet(self, request, queryset):
        nbr = len(queryset)
        for projet in queryset:
            projet.statut = 'C'
            projet.save(update_fields=['statut'])
        self.message_user(request, ngettext(
            '%(nbr)d projet fut cloturé avec succès.',
            '%(nbr)d projets furent cloturés avec succès.', nbr) % {'nbr': nbr}, messages.SUCCESS)

    cloturer_projet.short_description = "Cloturer les projets sélectionnés"

