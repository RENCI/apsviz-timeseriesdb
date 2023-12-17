from __future__ import unicode_literals
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter
from .serializers import gauge_station_source_data_Serializer, gauge_timemark_Serializer, gauge_station_Serializer, model_station_source_data_Serializer, model_timemark_Serializer
from .models import gauge_station_source_data, gauge_station, model_station_source_data
from rest_framework.pagination import PageNumberPagination

# Change page size dynamically by by using the psize variable in the URL
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'psize'

# Django view for All gauge and geometry view using the gauge_station_source_data_Serializer.
# The gauge_station_source_data_Serializer uses GeoFeatureModelSerializer which enables
# spatial searches
class drf_gauge_station_source_data_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = gauge_station_source_data.objects.all().order_by('time')
    serializer_class = gauge_station_source_data_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['obs_id','source_id','station_id','station_name','timemark','time','water_level','wave_height','wind_speed','air_pressure','flow_volume','stream_elevation','tz','units','gauge_owner','data_source','source_name','source_archive','location_name','location_type','apsviz_station','country','state','county','geom']

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

# Django view for All gauge and geometry view using the gauge_timemark_Serializer.
# The gauge_timemark_Serializer uses QueryFieldsMixin which enables the selection 
# of specific fields as output, but it conflicts with GeoFeatureModelSerializer
# so it has to have its own serializer and view
class drf_gauge_timemark_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = gauge_station_source_data.objects.distinct('timemark')
    serializer_class = gauge_timemark_Serializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['obs_id','source_id','station_id','station_name','timemark','time','water_level','wave_height','wind_speed','air_pressure','flow_volume','stream_elevation','tz',
                     'gauge_owner','data_source','source_name','source_archive','location_name','location_type','apsviz_station','country','state','county']

class drf_gauge_station_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = gauge_station.objects.all()
    serializer_class = gauge_station_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['station_id','station_name','tz','gauge_owner','location_name','location_type','apsviz_station','country','state','county','geom']

# Django view for all ADCIRC and geometry view using the model_timemark_Serializer.
# The model_timemark_Serializer uses QueryFieldsMixin which enables the selection
# of specific fields as output, but it conflicts with GeoFeatureModelSerializer
# so it has to have its own serializer and view
class drf_model_timemark_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = model_station_source_data.objects.distinct('timemark')
    serializer_class = model_timemark_Serializer 
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['model_id','source_id','station_id','station_name','timemark','time','model_run_id','water_level','wave_height','tz','gauge_owner','data_source',
                     'source_name','source_instance','source_archive','forcing_metaclass','location_name','location_type','apsviz_station','country','state','county']
        
class drf_gauge_station_View(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination
    queryset = gauge_station.objects.all()
    serializer_class = gauge_station_Serializer
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    filter_fields = ['station_id','station_name','tz','gauge_owner','location_name','location_type','apsviz_station','country','state','county','geom']
