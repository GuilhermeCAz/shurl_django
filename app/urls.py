from django.conf.urls import include
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

from app.views import URLViewSet, index

router = routers.DefaultRouter()
router.register('urls', URLViewSet, basename='URLs')

urlpatterns = [
    path('', index, name='index'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/', include(router.urls), name='api'),
    path(
        '<slug:slug>/',
        URLViewSet.as_view({'get': 'redirect_to_original'}),
        name='redirect_to_original',
    ),
]
