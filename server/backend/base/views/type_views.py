from base.models import Compaign, Type
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.serializers import TypeSerializer
from rest_framework.response import Response

## getters ------------------------
@api_view(["GET"])
def getTypes(request):
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getType(request, id):
    type = Type.objects.get(id=id)
    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getCompaignType(request, compaignID):
    compaign = Compaign.objects.get(id=compaignID)
    type = Type.objects.filter(compaign=compaign)
    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createType(request):
    data = request.data
    type = Type.objects.create(
        name=data["name"], coverImage=request.FILES.get("coverImage"), description=data["description"]
    )
    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateType(request, id):
    data = request.data
    type = Type.objects.get(id=id)
    type.name = data["name"]
    type.description = data["description"]
    type.coverImage = request.FILES.get("coverImage")
    type.save()

    serializer = TypeSerializer(type, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteType(request, id):
    type = Type.objects.get(id=id)
    type.delete()
    return Response("Type Deleted")
