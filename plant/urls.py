from django.urls import path, include
from rest_framework.routers import DefaultRouter

from plant.views import PlantViewSet

router = DefaultRouter()
router.register(r"plants", PlantViewSet)


urlpatterns = [
    path("", include(router.urls)),
]