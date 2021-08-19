from base.models import Step, Compaign, Type
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.serializers import StepSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

## getters ------------------------

## get all steps -------------------
@api_view(["GET"])
def getSteps(request):
    steps = Step.objects.all()
    serializer = StepSerializer(steps, many=True)
    return Response(serializer.data)


## get all type steps -------------------
@api_view(["GET"])
def getTypeSteps(request, typeID):
    type = Type.objects.get(id=typeID)
    steps = Step.objects.filter(type=type)
    serializer = StepSerializer(steps, many=True)
    return Response(serializer.data)


## get step by id -------------------
@api_view(["GET"])
def getStep(request, id):

    step = Step.objects.get(id=id)
    serializer = StepSerializer(step, many=True)
    return Response(serializer.data)


## step creator -----------------
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createStep(request):
    data = request.data
    type = Type.objects.get(data["type"])
    step = Step.objects.create(name=data["name"], type=type)
    serializer = StepSerializer(step, many=False)
    return Response(serializer.data)


## step updator -----------------
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateSteps(request, id):
    data = request.data
    step = Step.objects.get(id=id)
    step.name = data["name"]
    step.save()

    serializer = StepSerializer(step, many=False)
    return Response(serializer.data)


## step delete view -----------------
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteStep(request, id):
    step = Step.objects.get(id=id)
    step.delete()
    return Response("Step Deleted")
