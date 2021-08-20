from django.urls import path
from base.views import unit_views as views


urlpatterns = [
    path("register/", views.createUnit, name="create-unit"),
    path("update/<str:id>/", views.updateUnits, name="update-unit"),
    path("<str:id>/", views.getUnitById, name="get_unit"),
    path("", views.getAllUnits, name="get_units"),
    path("delete/<str:id>/", views.deleteUnit, name="delete_unit"),
]
