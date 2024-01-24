from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import gauge_station_source_data, gauge_station, model_station_source_data
from drf_queryfields import QueryFieldsMixin

# Serializer, with GeoFeatureModelSerializer, for tables for the gauge_station_source_data model view.
# GeoFeatureModelSerializer enables spatial searches. 
class gauge_station_source_data_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = gauge_station_source_data 
        geo_field = 'geom'
        id_field = 'obs_id'
        fields = ('obs_id','source_id','station_id','station_name','timemark','time','water_level','wave_height','wind_speed','air_pressure',
                  'stream_elevation','tz','units','gauge_owner','data_source','source_name','source_archive','location_name','location_type','apsviz_station',
                  'country','state','county')

# Serializer, with QueryFieldsMixin, for tables for the gauge_station_source_data model view
# QueryFieldsMixin enables the selection of specific fields as output, but it conflicts with 
# GeoFeatureModelSerializer so it has to have its own serializer
class gauge_timemark_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = gauge_station_source_data
        fields = ('obs_id','source_id','station_id','station_name','timemark','time','water_level','tz','gauge_owner','data_source','source_name','source_archive',
                  'location_name','location_type','country','state','county')

class gauge_station_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = gauge_station
        geo_field = 'geom'
        id_field = 'station_id'
        fields = ('station_id','station_name','tz','gauge_owner','location_name','location_type','apsviz_station','country','state','county')

# Serializer, with GeoFeatureModelSerializer, for tables for the gauge_station_source_data model view.
# GeoFeatureModelSerializer enables spatial searches.
class model_station_source_data_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = model_station_source_data
        geo_field = 'geom'
        id_field = 'model_id'
        fields = ('model_id','source_id','station_id','station_name','timemark','time','model_run_id','water_level','wave_height','tz','units','gauge_owner','data_source',
                  'source_name','source_instance','source_archive','forcing_metclass','location_name','location_type','apsviz_station','country','state','county')

# Serializer, with QueryFieldsMixin, for tables for the gauge_station_source_data model view
# QueryFieldsMixin enables the selection of specific fields as output, but it conflicts with
# GeoFeatureModelSerializer so it has to have its own serializer
class model_timemark_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = model_station_source_data
        fields = ('model_id','source_id','station_id','station_name','timemark','time','model_run_id','water_level','tz','gauge_owner','data_source','source_name',
                  'source_instance','source_archive','forcing_metclass','location_name','location_type','country','state','county')
