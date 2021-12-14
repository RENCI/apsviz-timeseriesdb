from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter
from .serializers import gauge_stations_observations_Serializer, nc_gauge_data_geom_Serializer, noaa_gauge_data_geom_Serializer
from .models import gauge_stations_observations, nc_gauge_data_geom, noaa_gauge_data_geom

# Django view for All gauge and geometry view
class drf_gauge_stations_observations_View(viewsets.ModelViewSet):
    queryset = gauge_stations_observations.objects.all()
    serializer_class = gauge_stations_observations_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['id','station','time','water_level','lat','lon','name','units','tz','owner','state','county']

    # Function to enable search by distance from lon/lat point
    @action(detail=False, methods=['get'])
    def get_nearest_gauges(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords),srid=4326)
            nearest_five_gauges = gauge_stations_observations.objects.annotate(distance=Distance('geom',user_location)).order_by('distance')[:10]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_five_gauges, many = True)
            print(nearest_five_gauges)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Django view for FIMAN gauge and geometry view
class drf_nc_gauge_data_geom_View(viewsets.ModelViewSet):
    queryset = nc_gauge_data_geom.objects.all()
    serializer_class = nc_gauge_data_geom_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['id','site_id','sensor_id','or_site_id','or_sensor_id','sensor_class','receive_time','data_time','data_value','raw_value','data_quality','units','county','name','owner','rain_only_gage','in_service','is_coastal']

    # Function to enable search by distance from lon/lat point
    @action(detail=False, methods=['get'])
    def get_nearest_gauges(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords),srid=4326)
            nearest_five_gauges = nc_gauge_data_geom.objects.annotate(distance=Distance('geom',user_location)).order_by('distance')[:10]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_five_gauges, many = True)
            print(nearest_five_gauges)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Django view for NOAAA gauge and geometry view
class drf_noaa_gauge_data_geom_View(viewsets.ModelViewSet):
    queryset = noaa_gauge_data_geom.objects.all()
    serializer_class = noaa_gauge_data_geom_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['id','gauge_name','date_time','water_level','sigma','flags','qc','provider','stationid','datatype','vertdatum']

