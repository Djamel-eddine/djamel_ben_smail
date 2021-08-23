from base.models import AssociationProfile, PersonProfile, Wilaya
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from base.serializers import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import uuid


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
def registerUser(request):
    data = request.data
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    user = User.objects.create(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        username=data["email"],
        is_staff=data["is_staff"],
        password=make_password(data["password"]),
        id=uuid.uuid4,
    )
    """ if data["is_staff"]:
        AssociationProfile.objects.create(
            user=user,
            phone=data["phone"],
            fax=data["fax"],
            name=data["name"],
            activity=data["activity"],
            associationNumber=data["associationNumber"],
            logo=data["logo"],
            coverImage=data["coverImage"],
            facebook=data["facebook"],
            twitter=data["twitter"],
            baseWilaya=wilaya,
        )
    else:
        PersonProfile.objects.create(
            user=user,
            phone=data["phone"],
            image=data["image"],
            isMale=data["isMale"],
            dateOfBirth=data["dateOfBirth"],
            profession=data["profession"],
            wilaya=wilaya,
            address=data["address"],
            address2=data["address2"],
        ) """

    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def registerUserAndProfile(request):
    data = request.data
    wilaya = Wilaya.objects.get(id=data["wilaya"])
    user = User.objects.create(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        username=data["email"],
        is_staff=data["is_staff"],
        password=make_password(data["password"]),
        id=uuid.uuid4,
    )
    if data["is_staff"]:
        AssociationProfile.objects.create(
            user=user,
            phone=data["phone"],
            fax=data["fax"],
            name=data["name"],
            activity=data["activity"],
            associationNumber=data["associationNumber"],
            logo=data["logo"],
            coverImage=data["coverImage"],
            facebook=data["facebook"],
            twitter=data["twitter"],
            baseWilaya=wilaya,
        )
    else:
        PersonProfile.objects.create(
            user=user,
            phone=data["phone"],
            image=data["image"],
            isMale=data["isMale"],
            dateOfBirth=data["dateOfBirth"],
            profession=data["profession"],
            wilaya=wilaya,
            address=data["address"],
            address2=data["address2"],
        )

    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data["firstname"]
    user.last_name = data["lastname"]
    user.username = data["email"]
    user.email = data["email"]

    if data["password"] != "":
        user.password = make_password(data["password"])

    user.save()

    return Response(serializer.data)


@api_view(["POST"])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    user.first_name = data["name"]
    user.username = data["email"]
    user.email = data["email"]
    user.is_staff = data["isAdmin"]

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response("User was deleted")
