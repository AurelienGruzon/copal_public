
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from copal_manager.models import Facture 
from api.serializers import FactureSerializer

# Create your views here:


@api_view(['GET', 'POST'])
def getFactures(request):

    if request.method == 'GET':
        factures = Facture.objects.all()
        serializer = FactureSerializer(factures, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = FactureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'PUT', 'DELETE'])
def getFactureDetails(request, id):

    try:
        facture = Facture.objects.get(id=id)
    except Facture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FactureSerializer(facture)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FactureSerializer(facture, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        facture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)