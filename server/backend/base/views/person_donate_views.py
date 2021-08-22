from base.models import PersonDonation, Compaign, Need
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.serializers import PersonDonationSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getPersonDonationsByCompaign(request, userID, compaignID):
    user = Compaign.objects.get(id=userID)
    compaign = User.objects.get(id=compaignID)
    donations = PersonDonation.objects.filter(user=user, compaign=compaign)
    serializer = PersonDonationSerializer(donations, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getPersonDonations(request, userID):
    user = User.objects.get(id=userID)
    donations = PersonDonation.objects.filter(user=user)
    serializer = PersonDonationSerializer(donations, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getCompaignDonations(request, compaignID):
    compaign = Compaign.objects.get(id=compaignID)
    donations = PersonDonation.objects.filter(compaign=compaign)
    serializer = PersonDonationSerializer(donations, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAssociationDonations(request, associationID):
    association = User.objects.get(id=associationID)
    donations = PersonDonation.objects.filter(association=association)
    serializer = PersonDonationSerializer(donations, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllDonations(request):
    donations = PersonDonation.objects.all()
    serializer = PersonDonationSerializer(donations, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getDonationById(request, id):
    compaign = Compaign.objects.get(id=id)
    donation = PersonDonation.objects.filter(compaign=compaign)
    serializer = PersonDonationSerializer(donation, many=False)
    return Response(serializer.data)


## donation creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createPersonDonation(request):
    data = request.data
    user = request.user
    compaign = Compaign.objects.get(id=data["compaign"])
    need = Need.objects.get(id=data["need"])
    donation = PersonDonation.objects.create(
        qteDonated=data["qteDonated"],
        user=user,
        compaign=compaign,
        need=need,
    )
    serializer = PersonDonationSerializer(donation, many=False)
    return Response(serializer.data)


## donation updator -----------------

## here the person part
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updatePersonDonation(request, id):
    data = request.data
    user = request.user
    donation = PersonDonation.objects.get(id=id)
    if donation.user == user:
        donation.qteDonated = data["qteDonated"]
        donation.save()
        serializer = PersonDonationSerializer(donation, many=False)
        return Response(serializer.data)


## here the Association part
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updatePersonDonationStatus(request, id):
    data = request.data
    donation = PersonDonation.objects.get(id=id)
    donation.status = data["status"]
    donation.qteAccepted = data["qteAccepted"]
    donation.qteDelivered = data["qteDelivered"]
    donation.save()

    serializer = PersonDonationSerializer(donation, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updatePersonDonationAcceptedQte(request, id):
    data = request.data
    donation = PersonDonation.objects.get(id=id)
    donation.qteAccepted = data["qteAccepted"]
    donation.save()

    serializer = PersonDonationSerializer(donation, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updatePersonDonationDeliverdQte(request, id):
    data = request.data
    donation = PersonDonation.objects.get(id=id)
    donation.qteDeliverd = data["qteDeliverd"]
    donation.save()
    serializer = PersonDonationSerializer(donation, many=False)
    return Response(serializer.data)


## donation delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletePersonDonation(request, id):
    donation = PersonDonation.objects.get(id=id)
    donation.delete()
    return Response("Donation Deleted")
