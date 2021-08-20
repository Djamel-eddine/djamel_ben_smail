from base.models import Wilaya
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import WilayaSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
def getAllWilayas(request):

    wilayas = Wilaya.objects.all()
    serializer = WilayaSerializer(wilayas, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getWilayaById(request, id):

    wilaya = Wilaya.objects.get(id=id)
    serializer = WilayaSerializer(wilaya, many=True)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createWilaya(request):
    data = request.data

    wilaya = Wilaya.objects.create(name=data["name"], number=data["number"])
    serializer = WilayaSerializer(wilaya, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateWilayas(request, id):
    data = request.data
    wilaya = Wilaya.objects.get(id=id)
    wilaya.name = data["name"]
    wilaya.number = data["number"]
    wilaya.save()

    serializer = WilayaSerializer(wilaya, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteWilaya(request, id):
    wilaya = Wilaya.objects.get(id=id)
    wilaya.delete()
    return Response("Wilaya Deleted")
