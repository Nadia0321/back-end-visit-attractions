from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
