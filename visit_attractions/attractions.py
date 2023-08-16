from django.db import models
from .places import Place
from .user import User
from django.contrib.postgres.fields import ArrayField


class Attraction(models.Model):
    name = models.CharField()
    likes = models.IntegerField(default=0)
    description = models.TextField()
    dislike = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    place_id = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='attraction')
    imageA = models.ImageField(upload_to='images/', blank=True, null=True)
    imageB = models.ImageField(upload_to='images/', blank=True, null=True)
    created_by = models.CharField(default='Nadia123')

    def __str__(self):
        return f"{self.place_id}, {self.name}"
