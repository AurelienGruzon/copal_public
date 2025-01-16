
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from copal_manager.models import Contrat 
from api.serializers import ContratSerializer

# Create your views here:


@api_view(['GET', 'POST'])
def getContrats(request):

    if request.method == 'GET':
        contrats = Contrat.objects.all()
        serializer = ContratSerializer(contrats, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ContratSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'PUT', 'DELETE'])
def getContratDetails(request, id):

    try:
        contrat = Contrat.objects.get(id=id)
    except Contrat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContratSerializer(contrat)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ContratSerializer(contrat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contrat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)