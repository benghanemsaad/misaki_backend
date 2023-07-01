from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Client
from .serializers import ClientSerializer

@api_view(['GET'])
def getAllClients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)