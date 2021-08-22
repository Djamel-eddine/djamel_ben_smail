from django.urls import path
from base.views import person_donate_views as views


urlpatterns = [
    path("register/", views.createPersonDonation, name="create-donation"),
    path("update/<str:id>/", views.updatePersonDonation, name="update-donation"),
    path("update_status/<str:id>/", views.updatePersonDonationStatus, name="update-donation-status"),
    path("update_accepted_qte/<str:id>/", views.updatePersonDonationAcceptedQte, name="update-donation-accepted-qte"),
    path("update_delivered_qte/<str:id>/", views.updatePersonDonationDeliverdQte, name="update-donation-delivered-qte"),
    path("", views.getAllDonations, name="get-donations"),
    path("<id:str>/", views.getDonationById, name="get-donation"),
    path("association?<str:associationID>/", views.getAssociationDonations, name="get_association_donations"),
    path(
        "user?<str:userID>/compaign?<compaignID>/",
        views.getPersonDonationsByCompaign,
        name="get_person_association_donations",
    ),
    path("user?<str:userID>/", views.getPersonDonations, name="get_person_donations"),
    path("compaign?<str:compaignID>/", views.getCompaignDonations, name="get_compaign_donations"),
    path("delete/<str:id>/", views.deletePersonDonation, name="delete_donation"),
]
