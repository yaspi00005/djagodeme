from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Don)
class DonAdmin(admin.ModelAdmin):
    list_display = ('id', 'montant', 'utilisateur', 'projet')
    list_filter = ['projet__secteur', 'projet__statut']
    search_fields = ['projet__nom', 'utilisateur__user__first_name', 'utilisateur__user__last_name']
    ordering = ('montant', 'projet__nom', 'utilisateur__user__first_name', 'utilisateur__user__last_name')
    fields = ('id', 'montant', 'utilisateur', 'projet')
    autocomplete_fields = ['utilisateur', 'projet']
    readonly_fields = ['id']


@admin.register(Financement)
class FinancementAdmin(admin.ModelAdmin):
    list_display = ('id', 'montant', 'date_debut', 'duree', 'projet', 'utilisateur')
    list_filter = ['projet__secteur', 'projet__statut']
    search_fields = ['projet__nom', 'utilisateur__user__first_name', 'utilisateur__user__last_name']
    ordering = ('montant', 'date_debut', 'duree', 'projet__nom', 'utilisateur__user__first_name', 'utilisateur__user__last_name')
    fields = ('id', 'montant', 'date_debut', 'duree', 'projet', 'utilisateur')
    autocomplete_fields = ['utilisateur', 'projet']
    readonly_fields = ['id']


@admin.register(Versement)
class VersementAdmin(admin.ModelAdmin):
    list_display = ['ref', 'date', 'motif', 'source', 'destination']
    list_filter = []
    search_fields = ['ref']
    ordering = ['ref', 'date']
    date_hierarchy = 'date'
    fieldsets = [
        ("Date et référence", {
            "fields": ("ref", "date")}),
        ("Type de versement", {
            "description": 'Choisir l\'un ou l\'autre',
            "classes": ["collapse", "start-open"],
            'fields': ('don', 'financement')}),
         ("Comptes d'opération", {
             "description": 'Remplissez le compte source et le compte destination',
             "classes": ["collapse", "start-open"],
             'fields': ('source', 'destination')})
    ]
    autocomplete_fields = ['don', 'financement', 'source', 'destination']
    readonly_fields = ['motif']
    save_on_top = True

    def motif(self, obj):
        if obj.don:
            return f"Dont de {obj.don.montant} FCFA"
        else:
            return f"Financement de {obj.financement.montant} FCFA"



class VersementInlineSource(admin.TabularInline):
    model = Versement
    fk_name = "source"
    verbose_name = 'Versement dont le compte est source'
    verbose_name_plural = "Versements dont le compte est source"
    extra = 0
    classes = ['collapse']


class VersementInlineDest(admin.TabularInline):
    model = Versement
    fk_name = "destination"
    verbose_name = 'Versement dont le compte est destination'
    verbose_name_plural = 'Versements dont le compte est destination'
    extra = 0
    classes = ['collapse']