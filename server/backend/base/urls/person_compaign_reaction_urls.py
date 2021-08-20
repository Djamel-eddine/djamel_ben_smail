from django.urls import path
from base.views import person_compaign_reaction_views as views


urlpatterns = [
    path("register/", views.createPersonCompaignReaction, name="create-reaction"),
    path("update/<str:id>/", views.updatePersonCompaignReactions, name="update-reaction"),
    path("compaign?<str:compaignID>/", views.getCompaignReactions, name="compaign_reaction"),
    path("user?<str:userID>/", views.getAllPersonCompaignReactions, name="compaign_reaction"),
    path("user?<str:userID>/compaign?<str:compaignID>/", views.getPersonCompaignReaction, name="get_reaction"),
    path("delete/<str:id>/", views.deletePersonCompaignReaction, name="delete_reaction"),
]
