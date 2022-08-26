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
from . import views
from .models import gauge_station_source_data, gauge_station

# Set URL for gauge geometry Django views
router = routers.DefaultRouter()

router.register(r'gauge_timemark', views.drf_gauge_timemark_View, 'gauge_timemark')
router.register(r'gauge_station_source_data', views.drf_gauge_station_source_data_View, 'gauge_station_source_data')
router.register(r'gauge_station', views.drf_gauge_station_View, 'gauge_station')

urlpatterns = [
    path("api/", include(router.urls)),
]
