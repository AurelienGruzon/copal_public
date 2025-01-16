
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from copal_manager.models import Prestation 
from api.serializers import PrestationSerializer

# Create your views here:

# Obtient la liste des prestations ou crée une nouvelle prestation
@api_view(['GET', 'POST'])
def getPrestations(request):

    if request.method == 'GET':
        prestations = Prestation.objects.all()
        serializer = PrestationSerializer(prestations, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PrestationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Obtient une prestation en particulier, la modifie ou la supprime        
@api_view(['GET', 'PUT', 'DELETE'])
def getPrestationDetails(request, id):

    try:
        prestation = Prestation.objects.get(id=id)
    except Prestation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PrestationSerializer(prestation)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PrestationSerializer(prestation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prestation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)