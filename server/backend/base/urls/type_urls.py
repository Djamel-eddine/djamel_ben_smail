from django.urls import path
from base.views import type_views as views


urlpatterns = [
    path("register/", views.createType, name="create-type"),
    path("update/<str:id>/", views.updateTypes, name="update-type"),
    path("compaign?<str:compaignID>/", views.getCompaignType, name="compaign_type"),
    path("<str:id>/", views.getType, name="get_type"),
    path("", views.getTypes, name="get_types"),
    path("delete/<str:id>/", views.deleteType, name="delete_type"),
]
