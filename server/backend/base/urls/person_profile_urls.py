from django.urls import path
from base.views import person_profile_views as views


urlpatterns = [
    path("register/", views.createPersonProfile, name="create-person-profile"),
    path("update/<str:id>/", views.updatePersonProfile, name="update-person-profile"),
    path("<str:id>/", views.getPersonProfile, name="get_person_profile_by_id"),
    path("", views.getPersonProfiles, name="get_persons"),
    path("delete/<str:id>/", views.deletePersonProfile, name="delete_person_profile"),
]
