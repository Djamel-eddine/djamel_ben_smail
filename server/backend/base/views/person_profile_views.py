from base.models import Compaign, PersonProfile, Wilaya
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.serializers import PersonProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
@permission_classes([IsAdminUser])
def getPersonProfiles(request):
    profiles = PersonProfile.objects.all()
    serializer = PersonProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getPersonProfile(request, id):
    user = User.objects.get(id=id)
    profile = PersonProfile.objects.get(user=user)
    serializer = PersonProfileSerializer(profile, many=False)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createPersonProfile(request):
    data = request.data
    user = request.user
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    profile = PersonProfile.objects.create(
        user=user,
        phone=data["phone"],
        isMale=data["isMale"],
        dateOfBirth=data["dateOfBirth"],
        profession=data["profession"],
        image=request.FILES.get("image"),
        wilaya=wilaya,
        address=data["address"],
        address2=data["address2"],
    )
    serializer = PersonProfileSerializer(profile, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updatePersonProfile(request, id):
    data = request.data
    user = User.objects.get(id=data["user"])
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    profile = PersonProfile.objects.get(user=user)
    profile.phone = data["phone"]
    profile.isMale = data["isMale"]
    profile.image = request.FILES.get("image")
    profile.wilaya = wilaya
    profile.dateOfBirth = data["dateOfBirth"]
    profile.profession = data["profession"]
    profile.address = data["address"]
    profile.address2 = data["address2"]
    profile.save()

    serializer = PersonProfileSerializer(type, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deletePersonProfile(request, id):
    user = User.objects.get(id=id)
    profile = PersonProfile.objects.get(user=user)
    profile.delete()
    return Response("Type Deleted")
