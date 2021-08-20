from django.urls import path
from base.views import need_views as views


urlpatterns = [
    path("register/", views.createNeed, name="create-need"),
    path("update/<str:id>/", views.updateNeed, name="update-need"),
    path("<str:id>/", views.getNeedById, name="get_need_by_id"),
    path("", views.getNeeds, name="get_needs"),
    path("delete/<str:id>/", views.deleteNeed, name="delete_need"),
]
