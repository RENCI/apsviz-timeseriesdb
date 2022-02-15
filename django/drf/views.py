from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter
from .serializers import gauge_station_source_data_Serializer
from .models import gauge_station_source_data

# Django view for All gauge and geometry view
class drf_gauge_station_source_data_View(viewsets.ModelViewSet):
    queryset = gauge_station_source_data.objects.all()
    serializer_class = gauge_station_source_data_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['obs_id','source_id','station_id','station_name','timemark','time','water_level','tz','gauge_owner','data_source','source_name','source_archive','location_name','location_type','country','state','county','geom']

    # Function to enable search by distance from lon/lat point
    @action(detail=False, methods=['get'])
    def get_nearest_gauges(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords),srid=4326)
            nearest_five_gauges = gauge_station_source_data.objects.annotate(distance=Distance('geom',user_location)).order_by('distance')[:10]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_five_gauges, many = True)
            print(nearest_five_gauges)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

