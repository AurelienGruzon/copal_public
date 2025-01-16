"""
URL configuration for copal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from copal_manager import views

#from api.views import ProprietaireViewset


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('api.urls')),
    path('', views.index, name = "index"),
    path('liste-proprietaires/', views.liste_proprietaires, name = "liste-proprietaires"),
    path('detail-proprietaires/<int:proprietaire_id>/', views.detail_proprietaire, name = "detail-proprietaire"),
    path('create-proprietaires/', views.create_proprietaire, name = "create-proprietaire"),
    path('liste-contrats/', views.liste_contrats, name = "liste-contrats"),
    path('detail-contrat/<int:contrat_id>', views.detail_contrat, name = "detail-contrat"),
    path('generer-contrat/<int:contrat_id>/', views.generer_contrat, name = "generer-contrat"),
    path('create-contrat/', views.create_contrat, name = "create-contrat"),
    path('liste-biens-immobiliers/', views.liste_biens_immobiliers, name = "liste-biens-immobiliers"),
    path('detail-bien-immobilier/<int:bien_immobilier_id>/', views.detail_bien_immobilier, name = "detail-bien-immobilier"),
    path('create-bien-immobilier/', views.create_bien_immobilier, name = "create-bien-immobilier"),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf')
    
]