from base.models import AssociationProfile, Wilaya
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.serializers import AssociationProfileSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
@permission_classes([IsAdminUser])
def getAssociationsProfiles(request):
    profiles = AssociationProfile.objects.all()
    serializer = AssociationProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getAssociationProfile(request, id):
    user = User.objects.get(id=id)
    profile = AssociationProfile.objects.get(user=user)
    serializer = AssociationProfileSerializer(profile, many=False)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createAssociationProfile(request):
    data = request.data
    user = request.user
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    profile = AssociationProfile.objects.create(
        user=user,
        phone=data["phone"],
        fax=data["fax"],
        name=data["name"],
        activity=data["activity"],
        associationNumber=data["associationNumber"],
        logo=request.FILES.get("logo"),
        coverImage=request.FILES.get("coverImage"),
        baseWilaya=wilaya,
        facebook=data["facebook"],
        twitter=data["twitter"],
    )
    serializer = AssociationProfileSerializer(profile, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateAssociationProfile(request, id):
    data = request.data
    user = User.objects.get(id=data["user"])
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    profile = AssociationProfile.objects.get(user=user)
    profile.phone = data["phone"]
    profile.fax = data["fax"]
    profile.name = data["name"]
    profile.activity = data["activity"]
    profile.associationNumber = data["associationNumber"]
    profile.logo = request.FILES.get("logo")
    profile.coverImage = request.FILES.get("coverImage")
    profile.baseWilaya = wilaya
    profile.facebook = data["facebook"]
    profile.twitter = data["twitter"]
    profile.save()

    serializer = AssociationProfileSerializer(type, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteAssociationProfile(request, id):
    user = User.objects.get(id=id)
    profile = AssociationProfile.objects.get(user=user)
    profile.delete()
    return Response("Type Deleted")
