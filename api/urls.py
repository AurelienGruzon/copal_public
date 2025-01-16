
from django.urls import path, include

from .views import proprietaires_views, contrats_views, biens_immobiliers_views, factures_views, prestations_views


urlpatterns = [
    path('api/proprietaires/', proprietaires_views.getProprietaires),
    path('api/proprietaires/<int:id>', proprietaires_views.getProprietaireDetails),
    path('api/contrats/', contrats_views.getContrats),
    path('api/contrats/<int:id>', proprietaires_views.getProprietaireDetails),
    path('api/biens_immobiliers/', biens_immobiliers_views.getBienImmobiliers),
    path('api/biens_immobiliers/<int:id>', biens_immobiliers_views.getBienImmobilierDetails),
    path('api/factures/', factures_views.getFactures),
    path('api/factures/<int:id>', factures_views.getFactureDetails),
    path('api/prestations/', prestations_views.getPrestations),
    path('api/prestations/<int:id>', prestations_views.getPrestationDetails),
]
