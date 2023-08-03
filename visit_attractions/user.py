from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    gmail = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000, default="")

    def __str__(self):
        return f"{self.name}"
