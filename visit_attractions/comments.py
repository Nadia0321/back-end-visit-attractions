from django.db import models


class Comment(models.Model):
    username = models.CharField(max_length=20)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description
