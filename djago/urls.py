from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('compte/nouveau', views.inscription, name='inscription'),
    path('compte/connexion', views.connexion, name='connexion'),
    path('compte/deconnexion', views.deconnexion, name='deconnexion'),
    path('search/<int:id_projet>', views.chercher_projet, name='searchProjet'),
    path('search/<int:budget>/<str:statut>', views.lister_projets, name='listeProjet'),
    path('search/<int:budget>/', views.lister_projets, name='listeProjet'),
    path('search/projets', views.liste_tous_projets, name='listeTousProjets'),
    path("newProjet", views.creerProjet, name="nouveauProjet"),
    path("contact", views.contact, name="contact"),
    path("profil", views.edit_profil, name="profile"),
    path("newSearch", views.search, name="newSearch")

]