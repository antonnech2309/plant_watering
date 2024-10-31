from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    watering_frequency_days = models.IntegerField()
    last_watered_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-last_watered_date"]
