from django.contrib import admin
from .places import Place
from .attractions import Attraction
from .comments import Comment


# Register your models here.
admin.site.register(Place)
admin.site.register(Attraction)
admin.site.register(Comment)
