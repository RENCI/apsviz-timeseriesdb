from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import gauge_stations_observations


# Serializer for tables holing data downloaded by Jeff's script
class gauge_stations_observations_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = gauge_stations_observations 
        geo_field = 'geom'
        id_field = 'obs_id'
        fields = ('obs_id','station_id','station_location_id','time','water_level','lat','lon','name','units','tz','owner','source_archive','country','state','county')

