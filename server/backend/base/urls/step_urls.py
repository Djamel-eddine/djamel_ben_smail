from django.urls import path
from base.views import step_views as views


urlpatterns = [
    path("register/", views.createStep, name="create-step"),
    path("update/<str:id>/", views.updateStep, name="update-step"),
    path("type?<str:typeID>/", views.getTypeSteps, name="type_steps"),
    path("<str:id>/", views.getStep, name="get_step"),
    path("", views.getSteps, name="get_steps"),
    path("delete/<str:id>/", views.deleteStep, name="delete_step"),
]
