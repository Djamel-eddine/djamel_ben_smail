from base.models import Unit
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import UnitSerializer
from rest_framework.response import Response

## getters ------------------------
@api_view(["GET"])
def getAllUnits(request):

    units = Unit.objects.all()
    serializer = UnitSerializer(units, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getUnitById(request, id):

    unit = Unit.objects.get(id=id)
    serializer = UnitSerializer(unit, many=True)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createUnit(request):
    data = request.data

    unit = Unit.objects.create(name=data["name"], acronym=data["acronym"], isFloat=data["isFloat"])
    serializer = UnitSerializer(unit, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUnits(request, id):
    data = request.data
    unit = Unit.objects.get(id=id)
    unit.name = data["name"]
    unit.acronym = data["acronym"]
    unit.isFloat = data["isFloat"]
    unit.save()

    serializer = UnitSerializer(unit, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteUnit(request, id):
    unit = Unit.objects.get(id=id)
    unit.delete()
    return Response("Unit Deleted")
