"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_mvt.views import mvt_view_factory
from . import views
from .models import nc_gauge_data_geom, noaa_gauge_data_geom 

# Set URL for gauge geometry Django views
router = routers.DefaultRouter()
router.register(r'nc_gauge_data_geom', views.drf_nc_gauge_data_geom_View)
router.register(r'noaa_gauge_data_geom', views.drf_noaa_gauge_data_geom_View)

urlpatterns = [
    path("api/", include(router.urls)),
]
