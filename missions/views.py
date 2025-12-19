from drf_spectacular.utils import extend_schema
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from missions.models import Mission, Target
from missions.serializers import (
    MissionSerializer,
    MissionCreateSerializer,
    TargetUpdateSerializer
)


@extend_schema(tags=["Missions"])
class MissionsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):

    def get_queryset(self):
        queryset = Mission.objects.all()
        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related(
                "cat"
            ).prefetch_related("targets")
        return queryset

    def get_serializer_class(self):
        if self.action == "create":
            return MissionCreateSerializer
        return MissionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.cat:
            return Response(
                data={"cat": "Cannot delete a mission with a cat assigned"},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)


@extend_schema(tags=["Missions"])
class TargetsViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetUpdateSerializer
