from datetime import datetime
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from plant.models import Plant
from plant.serializers import PlantSerializer


class PlantViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    @action(
        methods=["PATCH"],
        detail=True,
        url_path="update-last-watered",
        permission_classes=[],
    )
    def update_last_watered(self, request, pk=None):
        plant = self.get_object()
        last_watered_date = datetime.now()
        if last_watered_date:
            plant.last_watered_date = last_watered_date
            plant.save()
            return Response({"status": "last watered date updated", "last_watered_date": last_watered_date})
        return Response({"error": "last_watered_date not provided"}, status=400)
