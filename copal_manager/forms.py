from django import forms
from copal_manager.models import Proprietaire, Contrat, BienImmobilier
    
class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = '__all__'
        
class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'

class BienImmobilierForm(forms.ModelForm):
    class Meta:
        model = BienImmobilier
        fields = '__all__'
