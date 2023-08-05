from django.db import models
from .user import User
from .attractions import Attraction


class Comment(models.Model):
    description = models.CharField(max_length=300, default="")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=None, null=True)
    username = models.CharField(max_length=300, default="")
    attraction_id = models.ForeignKey(
        Attraction, on_delete=models.CASCADE, related_name='attraction', default=None, null=True)

    def __str__(self):
        return self.description
