from django.urls import path
from base.views import wilaya_views as views


urlpatterns = [
    path("register/", views.createWilaya, name="create-wilaya"),
    path("update/<str:id>/", views.updateWilayas, name="update-wilaya"),
    path("<str:id>/", views.getWilayaById, name="get_wilaya"),
    path("", views.getAllWilayas, name="get_wilayas"),
    path("delete/<str:id>/", views.deleteWilaya, name="delete_wilaya"),
]
