from django.db import models
from .user import User


class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")
    country = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='place', default=None, null=True)
    # image = models.ImageField(upload_to='images/', default='images/default_image.jpg')
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.name
