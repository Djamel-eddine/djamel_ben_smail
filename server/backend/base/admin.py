from django.contrib import admin
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
)

admin.site.register(Step)
admin.site.register(Type)
admin.site.register(PersonProfile)
admin.site.register(AssociationProfile)
admin.site.register(Comment)
admin.site.register(Compaign)
admin.site.register(Wilaya)
admin.site.register(Need)
admin.site.register(CompaignNeeds)
admin.site.register(CompaignSteps)
admin.site.register(AssociationWilayas)
