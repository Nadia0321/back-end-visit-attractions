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
    # user_id = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='attraction', default=None, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    # image = ArrayField(models.ImageField(
    #     upload_to='images/', blank=True, null=True), blank=True, null=True)

    def __str__(self):
        return f"{self.place_id}, {self.name}"
