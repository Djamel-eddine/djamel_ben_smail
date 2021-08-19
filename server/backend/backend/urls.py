"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", admin.site.urls),
    path("api/users/", include("base.urls.user_urls")),
    path("api/comments/", include("base.urls.comment_urls")),
    path("api/association_profile/", include("base.urls.association_profile_urls")),
    path("api/person_profile/", include("base.urls.person_profile_urls")),
    path("api/compaigns/", include("base.urls.compaign_urls")),
    path("api/needs/", include("base.urls.need_urls")),
    path("api/steps/", include("base.urls.step_urls")),
    path("api/types/", include("base.urls.type_urls")),
    path("api/wilayas/", include("base.urls.wilaya_urls")),
]
