import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from plant.models import Plant
from plant.serializers import PlantSerializer


class PlantApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.plant = Plant.objects.create(
            name="Rose",
            species="Flower",
            watering_frequency_days=3,
            last_watered_date="2021-09-01"
        )

    def test_get_plants(self):
        res = self.client.get(reverse("plant-list"))

        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_retreive_plant(self):
        res = self.client.get(reverse("plant-detail", args=[self.plant.id]))

        serializer = PlantSerializer(self.plant)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_create_plant(self):
        payload = {
            "name": "Lily",
            "species": "Flower",
            "watering_frequency_days": 2,
            "last_watered_date": "2021-09-01"
        }

        res = self.client.post(reverse("plant-list"), payload)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["name"], payload["name"])

    def test_update_plant(self):
        payload = {
            "name": "Lily",
            "species": "Flower",
            "watering_frequency_days": 2,
            "last_watered_date": "2021-09-01"
        }


        res = self.client.put(reverse("plant-detail", args=[self.plant.id]), payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], payload["name"])

    def test_update_only_last_watered_date(self):
        payload = {
            "last_watered_date": "2021-09-01"
        }

        res = self.client.patch(reverse("plant-detail", args=[self.plant.id]), payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["last_watered_date"], payload["last_watered_date"])

    def test_update_last_watered_date_automatically(self):
        payload = {}

        res = self.client.patch(reverse("plant-update-last-watered", args=[self.plant.id]), payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["last_watered_date"].date(), datetime.datetime.now().date())