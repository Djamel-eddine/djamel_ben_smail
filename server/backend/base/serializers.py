from .models import (
    Step,
    Type,
    PersonProfile,
    AssociationProfile,
    Comment,
    Compaign,
    Wilaya,
    Need,
    CompaignNeeds,
    CompaignSteps,
    AssociationWilayas,
    Unit,
    PersonDonation,
    PersonCompaignReaction,
    Notifications,
)
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class PersonDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDonation
        fields = "__all__"


class PersonCompaignReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCompaignReaction
        fields = "__all__"


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CompaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compaign
        fields = "__all__"


class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = "__all__"


class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class CompaignNeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaignNeeds
        fields = "__all__"


class CompaignStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaignSteps
        fields = "__all__"


class AssociationWilayasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociationWilayas
        fields = "__all__"


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


""" user serializer ------------------------------------ """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "is_staff",
        ]

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == "":
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "token",
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class PersonProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonProfile
        fields = "__all__"


class AssociationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociationProfile
        fields = "__all__"
