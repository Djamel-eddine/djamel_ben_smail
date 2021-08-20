from base.models import Need, Unit
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import NeedSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
def getNeeds(request):

    need = Need.objects.all()
    serializer = NeedSerializer(need, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNeedById(request, id):

    need = Need.objects.filter(id=id)
    serializer = NeedSerializer(need, many=True)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createNeed(request):
    data = request.data
    unit = Unit.objects.get(id=data["unit"])
    need = Need.objects.create(name=data["name"], description=data["description"], unit=unit)
    serializer = NeedSerializer(need, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateNeed(request, id):
    data = request.data
    unit = Unit.objects.get(id=data["unit"])
    need = Need.objects.get(id=id)
    need.name = data["name"]
    need.description = data["description"]
    need.unit = unit
    need.save()

    serializer = NeedSerializer(need, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteNeed(request, id):
    comment = Need.objects.get(id=id)
    comment.delete()
    return Response("Need Deleted")
