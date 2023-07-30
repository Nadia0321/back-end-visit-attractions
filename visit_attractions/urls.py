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
    # path('places/<str:place_id>/', views.get_one_place),
    # path('places/<int:id>/attractions', views.attractions_list),
    # path('places/<int:place_id>/attractions/<int:attr_id>', views.one_attraction),
    path('admin/', admin.site.urls),

    # path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    # path('home/', views.HomeView.as_view(), name ='home'),
    # path('logout/', views.LogoutView.as_view(), name ='logout'),
    # path('', include('visit_attractions.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
