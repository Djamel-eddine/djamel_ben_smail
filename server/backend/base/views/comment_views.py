from base.models import Comment, Compaign
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import CommentSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------
@api_view(["GET"])
def getUserCommentsByCompaign(request, userID, compaignID):
    user = Compaign.objects.get(id=userID)
    compaign = User.objects.get(id=compaignID)
    comments = Comment.objects.filter(user=user, compaign=compaign)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getUserComments(request, userID):
    user = User.objects.get(id=userID)
    comments = Comment.objects.filter(user=user)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCompaignComments(request, compaignID):
    compaign = Compaign.objects.get(id=compaignID)
    comments = Comment.objects.filter(compaign=compaign)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


## comment creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createComment(request):
    data = request.data
    user = User.objects.get(id=data["user"])
    compaign = Compaign.objects.get(id=data["compaign"])
    comment = Comment.objects.create(payload=data["payload"], title=data["title"], user=user, compaign=compaign)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


## comment updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateComments(request, id):
    data = request.data
    comment = Comment.objects.get(id=id)
    comment.payload = data["payload"]
    comment.title = data["title"]
    comment.save()

    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


## comment delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteComment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return Response("Comment Deleted")
