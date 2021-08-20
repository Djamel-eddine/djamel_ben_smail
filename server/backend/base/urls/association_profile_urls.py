from django.urls import path
from base.views import association_profile_views as views


urlpatterns = [
    path("register/", views.createAssociationProfile, name="create-association-profile"),
    path("update/<str:id>/", views.updateAssociationProfile, name="update-association-profile"),
    path("<str:id>/", views.getAssociationProfile, name="get_association_profile_by_id"),
    path("", views.getAssociationsProfiles, name="get_associations"),
    path("delete/<str:id>/", views.deleteAssociationProfile, name="delete_association_profile"),
]
