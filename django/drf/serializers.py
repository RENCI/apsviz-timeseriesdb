from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import gauge_stations_observations, nc_gauge_data_geom, noaa_gauge_data_geom


# Serializer for tables holing data downloaded by Jeff's script
class gauge_stations_observations_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = gauge_stations_observations 
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','station','time','water_level','lat','lon','name','units','tz','owner','state','county')

# Serializer for FIMAN gauges
class nc_gauge_data_geom_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = nc_gauge_data_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','site_id','sensor_id','or_site_id','or_sensor_id','sensor_class','receive_time','data_time','data_value','raw_value','data_quality','units','county','name','owner','rain_only_gage','in_service','is_coastal')

# Serializer for NOAA gauges
class noaa_gauge_data_geom_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = noaa_gauge_data_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','gauge_name','date_time','water_level','sigma','flags','qc','provider','stationid','datatype','vertdatum')

