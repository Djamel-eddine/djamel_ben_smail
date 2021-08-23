from backend.base.constants.donation_status import DonationStatus
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from base.models import Compaign, PersonCompaignReaction, PersonDonation, CompaignNeeds
import datetime


def updateCompaignNeedQTE(sender, instance, created, **kwargs):
    donation = instance
    compaignNeed = CompaignNeeds.objects.get(id=donation.compaignNeed)

    if created:
        print("new donation received")

    else:
        if donation.status == DonationStatus.accepted:
            compaignNeed.qteAccepted += donation.qteAccepted
        elif donation.status == DonationStatus.delivered:
            compaignNeed.qteDonated += donation.qteDelivered
        elif donation.status == DonationStatus.refused:
            qtePreAccepted = donation.qteAccepted
            if qtePreAccepted == 0:
                compaignNeed.qteDonated += donation.qteDelivered
            else:
                compaignNeed.qteAccepted -= qtePreAccepted
                compaignNeed.qteDonated += donation.qteDelivered
        compaignNeed.save()


pre_save.connect(updateCompaignNeedQTE, sender=PersonDonation)


def updateCompaignReaction(sender, instance, created, **kwargs):
    reaction = instance
    compaign = Compaign.objects.get(id=reaction.compaign)

    if created:
        if reaction.isLike:
            compaign.likes += 1
        else:
            compaign.dislikes += 1

    else:
        if reaction.isLike:
            compaign.likes -= 1
            compaign.dislikes += 1
        else:
            compaign.likes += 1
            compaign.dislikes -= 1
    compaign.save()


pre_save.connect(updateCompaignReaction, sender=PersonCompaignReaction)
