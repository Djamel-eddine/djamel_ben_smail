from django.db import models
from django.contrib.auth.models import User
import uuid

## profile of a person -not an association- --------------------
class PersonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, default="")
    dateOfBirth = models.DateTimeField(auto_now_add=False, default="")
    profession = models.CharField(max_length=50, default="")
    wilaya = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user.username


## association profile --------------------
class AssociationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, default="")
    fax = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50)
    activity = models.CharField(max_length=200)
    associationNumber = models.CharField(max_length=200)
    logo = models.CharField(max_length=50, default="")
    baseWilaya = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## type of compaigns --------------------
class Type(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of needs --------------------
class Need(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of steps --------------------
class Step(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of wilayas --------------------------------------
class Wilaya(models.Model):

    number = models.IntegerField(null=True, blank=False)
    name = models.CharField(max_length=50, null=True, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## compaign core ---------------------------------
class Compaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    association = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    GPS = models.CharField(max_length=50, default="")
    daira = models.CharField(max_length=50, default="")
    baladia = models.CharField(max_length=50, default="")
    image_url = models.CharField(max_length=50, default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name


## list of the wilayas where the associations is active --------------------
class AssociationWilayas(models.Model):

    association = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.association.name


## list of the needs that the compaign needs --------------------
class CompaignNeeds(models.Model):

    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null=False)
    need = models.ForeignKey(Need, on_delete=models.CASCADE, null=False)
    qte = models.IntegerField(null=True, blank=False)
    qteDonated = models.IntegerField(null=True, blank=False, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.compaign.name


## list of the steps in compaign --------------------
class CompaignSteps(models.Model):

    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null=False)
    step = models.ForeignKey(Step, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=200, default="")
    range = models.IntegerField(null=True, blank=False)
    isDone = models.BooleanField(null=True, blank=False, default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.compaign.name


##comments --------------------------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=True, blank=False)
    payload = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title
