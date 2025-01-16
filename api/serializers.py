from rest_framework.serializers import ModelSerializer 

from copal_manager.models import Proprietaire, Contrat, BienImmobilier, Facture, Prestation

class ProprietaireSerializer(ModelSerializer):

    class Meta:
        model = Proprietaire
        fields = '__all__'

class ContratSerializer(ModelSerializer):

    class Meta:
        model = Contrat
        fields = '__all__'

class BienImmobilierSerializer(ModelSerializer):

    class Meta:
        model = BienImmobilier
        fields = '__all__'

class FactureSerializer(ModelSerializer):

    class Meta:
        model = Facture
        fields = '__all__'

class PrestationSerializer(ModelSerializer):

    class Meta:
        model = Prestation
        fields = '__all__'
