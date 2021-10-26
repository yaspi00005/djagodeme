from django.urls import path
from . import views
from deme import views

urlpatterns = [
    path('don', views.FaireDon, name='don'),
    path('donate/<int:id_projet>', views.FaireDonProjet, name='donate'),
    path('search/dons', views.liste_tous_dons, name='liste_tous_dons'),
    path('search/fiancement', views.liste_financement, name='liste_financement'),
]
