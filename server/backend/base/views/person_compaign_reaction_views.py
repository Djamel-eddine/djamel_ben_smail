from base.models import PersonCompaignReaction, Compaign
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import PersonCompaignReactionSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
def getAllPersonCompaignReactions(request, userID):
    user = User.objects.get(id=userID)
    reactions = PersonCompaignReaction.objects.filter(user=user)
    serializer = PersonCompaignReactionSerializer(reactions, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getPersonCompaignReaction(request, userID, compaignID):
    user = User.objects.get(id=userID)
    compaign = Compaign.objects.get(id=compaignID)
    reaction = PersonCompaignReaction.objects.filter(user=user, compaign=compaign)
    serializer = PersonCompaignReactionSerializer(reaction, many=False)
    return Response(serializer.data)


def getCompaignReactions(request, compaignID):
    compaign = Compaign.objects.get(id=compaignID)
    reactions = PersonCompaignReaction.objects.filter(compaign=compaign)
    serializer = PersonCompaignReactionSerializer(reactions, many=True)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createPersonCompaignReaction(request):
    data = request.data
    user = User.objects.get(id=data["user"])
    compaign = Compaign.objects.get(id=data["compaign"])
    wilaya = PersonCompaignReaction.objects.create(user=user, compaign=compaign, isLike=data["isLike"])
    serializer = PersonCompaignReactionSerializer(wilaya, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updatePersonCompaignReactions(request, id):
    data = request.data
    reaction = PersonCompaignReaction.objects.get(id=id)
    reaction.isLike = data["isLike"]
    reaction.save()

    serializer = PersonCompaignReactionSerializer(reaction, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletePersonCompaignReaction(request, id):
    wilaya = PersonCompaignReaction.objects.get(id=id)
    wilaya.delete()
    return Response("Person reaction on compaign deleted")
