from django.urls import path
from . import views
from deme import views

urlpatterns = [
    path('don', views.FaireDon, name='don'),
    path('donate/<int:id_projet>', views.FaireDonProjet, name='donate'),
    path('search/dons', views.liste_tous_dons, name='liste_tous_dons'),
    path('list/dons/<int:id_projet>/', views.donliste, name='liste_tous_dons'),
    path('list/fiancement/<int:id_projet>/',
         views.liste_financement, name='listefinancement'),
    path('financer/<int:id_projet>', views.financerprojet, name='financer'),
    # path('search/<int:budget>/', views.lister_don, name='listeDon'),


]
