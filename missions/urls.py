from django.urls import path, include
from rest_framework import routers

from missions.views import TargetsViewSet, MissionsViewSet

router = routers.DefaultRouter()
router.register("targets", TargetsViewSet, basename="targets")
router.register("missions", MissionsViewSet, basename="missions")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "missions"