from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import gauge_station_source_data


# Serializer for tables holing data downloaded by Jeff's script
class gauge_station_source_data_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = gauge_station_source_data 
        geo_field = 'geom'
        id_field = 'obs_id'
        fields = ('obs_id','source_id','station_id','station_name','timemark','time','water_level','tz','gauge_owner','data_source','source_name','source_archive','location_name','location_type','country','state','county')

