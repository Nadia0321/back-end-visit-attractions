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
from django.urls import path, include
# from rest_framework_simplejwt import views as jwt_views
from visit_attractions import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # this is like the blueprint in Flask, the routes start with places/,
    # unlike Flask, we need to add / after the endpoint
    path('places/', views.get_place_list),
    path('places/', views.post_place),
    path('places/<int:place_id>/', views.get_one_place),
    path('places/<int:place_id>/', views.delete_one_place),
    path('places/<int:place_id>/attractions/', views.get_place_attractions),
    path('places/<int:place_id>/attractions/', views.create_attraction),
    path('places/<int:place_id>/attractions/<int:attraction_id>',
         views.delete_attraction),
    path('users/<str:username>/', views.get_user),
    path('users/', views.post_user),

    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
