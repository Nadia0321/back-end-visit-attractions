from django.db import models
from .places import Place
from .user import User


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    likes = models.IntegerField()
    description = models.CharField(max_length=100, default="")
    dislike = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    place_id = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='attraction')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='attraction', default=None, null=True)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.place_id}, {self.name}"
