from base.models import Wilaya
from base.models import Compaign, Type
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import CompaignSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

##TODO the search and pagination remains
## getters ------------------------
@api_view(["GET"])
def getAllCompaigns(request):
    compaigns = Compaign.objects.all()
    serializer = CompaignSerializer(compaigns, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAssociationCompaigns(request, userID):
    user = Compaign.objects.get(id=userID)
    compaigns = Compaign.objects.filter(user=user)
    serializer = CompaignSerializer(compaigns, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getTypeCompaigns(request, typeId):
    type = Type.objects.get(id=typeId)
    compaigns = Compaign.objects.filter(type=type)
    serializer = CompaignSerializer(compaigns, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getWilayaCompaigns(request, wilayaId):
    wilaya = Wilaya.objects.get(id=wilayaId)
    compaigns = Compaign.objects.filter(wilaya=wilaya)
    serializer = CompaignSerializer(compaigns, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCompaignById(request, id):
    compaign = Compaign.objects.get(id=id)
    serializer = CompaignSerializer(compaign, many=False)
    return Response(serializer.data)


## compaign creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createCompaign(request):
    data = request.data
    user = request.user
    type = Type.objects.get(id=data["type"])
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    compaign = Compaign.objects.create(
        name=data["name"],
        start=data["start"],
        end=data["end"],
        description=data["description"],
        association=user,
        wilaya=wilaya,
        type=type,
        GPS=data["GPS"],
        daira=data["daira"],
        baladia=data["baladia"],
        image=request.FILES.get("image"),
    )
    serializer = CompaignSerializer(compaign, many=False)
    return Response(serializer.data)


## compaign updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateCompaign(request, id):
    data = request.data
    type = Type.objects.get(id=data["type"])
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    compaign = Compaign.objects.get(id=id)
    compaign.name = data["name"]
    compaign.start = data["start"]
    compaign.end = data["end"]
    compaign.description = data["description"]
    compaign.type = type
    compaign.wilaya = wilaya
    compaign.GPS = data["GPS"]
    compaign.daira = data["daira"]
    compaign.baladia = data["baladia"]
    compaign.save()

    serializer = CompaignSerializer(compaign, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateCompaignImage(request, id):
    compaign = Compaign.objects.get(id=id)
    compaign.image = request.FILES.get("image")
    compaign.save()

    serializer = CompaignSerializer(compaign, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateCompaignIsDone(request, id):
    data = request.data
    compaign = Compaign.objects.get(id=id)
    compaign.isDone = data["isDone"]
    compaign.save()

    serializer = CompaignSerializer(compaign, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateCompaignIsArchived(request, id):
    data = request.data
    compaign = Compaign.objects.get(id=id)
    compaign.isArchived = data["isArchived"]
    compaign.save()

    serializer = CompaignSerializer(compaign, many=False)
    return Response(serializer.data)


## compaign delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteCompaign(request, id):
    compaign = Compaign.objects.get(id=id)
    compaign.delete()
    return Response("Compaign Deleted")
