from django.db import models
from .places import Place


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    likes = models.IntegerField()
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='attraction')

    def __str__(self):
        return f"{self.place}, {self.name}"
