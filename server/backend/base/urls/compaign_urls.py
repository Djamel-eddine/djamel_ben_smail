from django.urls import path
from base.views import compaign_views as views


urlpatterns = [
    path("register/", views.createCompaign, name="create-compaign"),
    path("update/<str:id>/", views.updateCompaign, name="update-compaign"),
    path("update_image/<str:id>/", views.updateCompaign, name="update-compaign-image"),
    path("update_done/<str:id>/", views.updateCompaign, name="update-compaign-done"),
    path("update_archived/<str:id>/", views.updateCompaign, name="update-compaign-archived"),
    path("", views.getAllCompaigns, name="get-compaigns"),
    path("<id:str>/", views.getAllCompaigns, name="get-compaign"),
    path("association?<str:userID>/", views.getAssociationCompaigns, name="get_association_compaigns"),
    path("type?<str:typeID>/", views.getTypeCompaigns, name="type_compaign_compaigns"),
    path("wilaya?<str:wilayaID>/", views.getWilayaCompaigns, name="wilaya_compaign_compaigns"),
    path("delete/<str:id>/", views.deleteCompaign, name="delete_compaign"),
]
