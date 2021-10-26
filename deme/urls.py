from django.urls import path
from . import views
from deme import views

urlpatterns = [
    path('don', views.FaireDon, name='don'),
    path('finacement', views.FaireFinacement, name='financement'),
    path('search/dons', views.liste_tous_dons, name='liste_tous_dons'),
    path('search/<int:id_projet>/',
         views.liste_financement, name='listefinancement'),
    path('search/<int:budget>/', views.lister_don, name='listeDon'),


]
