import enum
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.aggregates import Max
from django.db.models.fields import BLANK_CHOICE_DASH


## list of wilayas --------------------------------------
class Wilaya(models.Model):

    number = models.IntegerField(blank=False, default = 1)
    name = models.CharField(max_length=50, blank=False, default= '')
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## profile of a person -not an association- --------------------
class PersonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, default="")
    image = models.ImageField(null=True, blank=True)
    isMale = models.BooleanField(default=True)
    dateOfBirth = models.DateTimeField(auto_now_add=False, default="")
    profession = models.CharField(max_length=100, default="")
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, null= True)
    address = models.CharField(max_length=200, blank=True, default="")
    address2 = models.CharField(max_length=200, blank=True, default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username


## association profile --------------------
class AssociationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, default="")
    fax = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default = '')
    activity = models.CharField(max_length=200)
    associationNumber = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True)
    coverImage = models.ImageField(null=True, blank=True)
    baseWilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, null= True)
    facebook = models.CharField(max_length=50, blank=True, default="")
    twitter = models.CharField(max_length=50, blank=True, default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## type of compaigns --------------------
class Type(models.Model):

    name = models.CharField(max_length=50, blank=False, default ='')
    description = models.CharField(max_length=200, blank=True, default="")
    coverImage = models.ImageField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## need units ---------------------------
class Unit(models.Model):

    name = models.CharField(max_length=50, blank=False, default ='')
    acronym = models.CharField(max_length=5, blank=True)
    isFloat = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of needs --------------------
class Need(models.Model):

    name = models.CharField(max_length=50, blank=False, default = '')
    description = models.CharField(max_length=200, blank=True, default = '')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null= True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of steps --------------------
class Step(models.Model):

    name = models.CharField(max_length=50, blank=False, default = '')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null = True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## compaign core ---------------------------------
class Compaign(models.Model):
    name = models.CharField(max_length=50, blank=False, default = '')
    start = models.DateTimeField(auto_now_add=False, blank=False)
    end = models.DateTimeField(auto_now_add=False, blank=False)
    description = models.CharField(max_length=200, default="")
    association = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, null= True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null= True)
    GPS = models.CharField(max_length=200, default="")
    daira = models.CharField(max_length=50, default="")
    baladia = models.CharField(max_length=50, default="")
    image = models.ImageField(null=True, blank=True)
    isDone = models.BooleanField(default=False)
    isArchived = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of the wilayas where the associations is active --------------------
class AssociationWilayas(models.Model):

    association = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, null= True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.association.username


## list of the needs that the compaign needs --------------------
class CompaignNeeds(models.Model):

    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null= True)
    need = models.ForeignKey(Need, on_delete=models.CASCADE, null= True)
    description = models.CharField(max_length=200, blank=True, default="")
    level = models.PositiveIntegerField(default=1)
    qteRequested = models.FloatField(blank=False, default= 1)
    qteDonated = models.FloatField(blank=False, default=0)
    qteAccepted = models.FloatField(blank=False, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.compaign.name


## list of the steps in compaign --------------------
class CompaignSteps(models.Model):

    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null= True)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, null= True)
    description = models.CharField(max_length=200, default="")
    range = models.IntegerField(blank=False, default = 1)
    isDone = models.BooleanField(blank=False, default=False)
    completeDate = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.compaign.name


##comments --------------------------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=50, null=True, blank=False)
    payload = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title


##store the person donations --------------------------
class PersonDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null= True)
    need = models.ForeignKey(Need, on_delete=models.CASCADE, null= True)
    qte = models.FloatField(default=1)
    status = models.FloatField(default=1)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username


##store the person reaction on compaign --------------------------
class PersonCompaignReaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE)
    isLike = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username


##store the person notifications --------------------------
class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    message = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=200, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username
