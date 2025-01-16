
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from copal_manager.models import Proprietaire 
from api.serializers import ProprietaireSerializer

# Create your views here:

# Obtient la liste des propriétaires ou crée un nouveau propriétaire
@api_view(['GET', 'POST'])
def getProprietaires(request):

    if request.method == 'GET':
        proprietaires = Proprietaire.objects.all()
        serializer = ProprietaireSerializer(proprietaires, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProprietaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

# Obtient un propriétaire en particulier, le modifie ou le supprime
@api_view(['GET', 'PUT', 'DELETE'])
def getProprietaireDetails(request, id):

    try:
        proprietaire = Proprietaire.objects.get(id=id)
    except Proprietaire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProprietaireSerializer(proprietaire)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProprietaireSerializer(proprietaire, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        proprietaire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)