from django.conf.urls.static import static

from django.urls import path, include
from drf_spectacular.views import (
    SpectacularYAMLAPIView,
    SpectacularJSONAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView)

from sca_backend import settings

urlpatterns = [
    path("api/v1/", include("cats.urls", namespace="cats")),
    path("api/v1/", include("missions.urls", namespace="missions")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [path("yml/", SpectacularYAMLAPIView.as_view(), name="yml-schema")]
    urlpatterns += [path("json/", SpectacularJSONAPIView.as_view(), name="schema")]
    urlpatterns += [
        path(
            "swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        )
    ]
    urlpatterns += [path("redoc/", SpectacularRedocView.as_view(), name="redoc")]
