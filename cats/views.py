from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from cats.models import Cat
from cats.serializers import CatSerializer, CatUpdateSerializer

@extend_schema(tags=["Cats"])
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return CatUpdateSerializer
        return CatSerializer
