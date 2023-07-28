"""
URL configuration for visit_attractions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from visit_attractions import views

urlpatterns = [
    # this is like the blueprint in Flask, the routes start with places/,
    # unlike Flask, we need to add / after the endpoint
    path('places/', views.place_list),
    path('places/<int:place_id>/', views.get_one_place),
    # path('places/<int:id>/attractions', views.attractions_list),
    # path('places/<int:place_id>/attractions/<int:attr_id>', views.one_attraction),
    path('admin/', admin.site.urls),
]
