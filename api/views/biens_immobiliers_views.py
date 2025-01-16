
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from copal_manager.models import BienImmobilier
from api.serializers import BienImmobilierSerializer

# Create your views here:


@api_view(['GET', 'POST'])
def getBienImmobiliers(request):

    if request.method == 'GET':
        biens_immobiliers = BienImmobilier.objects.all()
        serializer = BienImmobilierSerializer(biens_immobiliers, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BienImmobilierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'PUT', 'DELETE'])
def getBienImmobilierDetails(request, id):

    try:
        bien_immobilier = BienImmobilier.objects.get(id=id)
    except BienImmobilier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BienImmobilierSerializer(bien_immobilier)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BienImmobilierSerializer(bien_immobilier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bien_immobilier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)