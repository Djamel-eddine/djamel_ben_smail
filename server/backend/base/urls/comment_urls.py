from django.urls import path
from base.views import comment_views as views


urlpatterns = [
    path("register/", views.createComment, name="create-comment"),
    path("update/<str:id>/", views.updateComments, name="update-comment"),
    path("compaign/<str:compaignID>/", views.getCompaignComments, name="compaign_comments"),
    path("user/<str:userID>/", views.getUserComments, name="user_comments"),
    path(
        "compaign/<str:compaignID>/user/<str:userID>/", views.getUserCommentsByCompaign, name="user_compaign_comments"
    ),
    path("delete/<str:id>/", views.deleteComment, name="delete_comment"),
]
