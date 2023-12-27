from __future__ import unicode_literals
from django.contrib.gis.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

# Model for source observation meta, which is used as input for scripts
class source_obs_meta(models.Model):
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(20,null=False)
    source_archive = models.TextField(15,null=False)
    source_variable = models.TextField(15,null=False)
    filename_prefix = models.TextField(100,null=False)
    location_type = models.TextField(10,null=False)
    data_type = models.TextField(6,null=False)
    units = models.TextField(10,null=True)

# Model for source ADCIRC model meta, which is used as input for scripts
class source_model_meta(models.Model):
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(20,null=False)
    source_archive = models.TextField(15,null=False)
    source_variable = models.TextField(15,null=False)
    source_instance = models.TextField(25,null=False)
    forcing_metaclass = models.TextField(15,null=False)
    filename_prefix = models.TextField(100,null=False)
    location_type = models.TextField(10,null=False)
    units = models.TextField(10,null=True)

# Model for archiving the harvesting gauge observation data files meta-data
class harvest_obs_file_meta(models.Model):
    file_id = models.AutoField(primary_key=True)
    dir_path = models.TextField(100,null=False)
    file_name = models.TextField(100,null=False)
    data_date_time = models.DateTimeField(null=True) 
    data_begin_time = models.DateTimeField(null=True)
    data_end_time = models.DateTimeField(null=True)
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(30,null=False)
    source_archive = models.TextField(30,null=False)
    source_variable = models.TextField(15,null=False)
    location_type = models.TextField(10,null=False)
    timemark = models.DateTimeField(null=True)
    processing_datetime = models.DateTimeField(null=True)
    ingested = models.BooleanField(null=False)
    overlap_past_file_date_time = models.BooleanField(null=False)

# Model for archiving the harvesting gauge observation data files meta-data
class harvest_model_file_meta(models.Model):
    file_id = models.AutoField(primary_key=True)
    dir_path = models.TextField(100,null=False)
    file_name = models.TextField(100,null=False)
    data_date_time = models.DateTimeField(null=True) 
    data_begin_time = models.DateTimeField(null=True)
    data_end_time = models.DateTimeField(null=True)
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(30,null=False)
    source_archive = models.TextField(30,null=False)
    source_instance = models.TextField(25,null=False)
    forcing_metaclass = models.TextField(15,null=False)
    advisory = models.TextField(40,null=True)
    model_run_id = models.TextField(40,null=True)
    timemark = models.DateTimeField(null=True)
    processing_datetime = models.DateTimeField(null=True)
    ingested = models.BooleanField(null=False)
    overlap_past_file_date_time = models.BooleanField(null=False)

# Model for archiving the apsViz station files meta-data
class apsviz_station_file_meta(models.Model):
    file_id = models.AutoField(primary_key=True)
    dir_path = models.TextField(100,null=False)
    file_name = models.TextField(100,null=False)
    data_date_time = models.DateTimeField(null=True)
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(30,null=False)
    source_archive = models.TextField(30,null=False)
    source_instance = models.TextField(25,null=False)
    forcing_metaclass = models.TextField(15,null=False)
    grid_name = models.TextField(30,null=False)
    model_run_id = models.TextField(40,null=True)
    timemark = models.DateTimeField(null=False)
    location_type = models.TextField(8,null=False)
    csvurl =  models.TextField(100,null=True)
    ingested = models.BooleanField(null=False)

# Model for archiving the apsViz station files meta-data
class retain_obs_station_file_meta(models.Model):
    file_id = models.AutoField(primary_key=True)
    dir_path = models.TextField(100,null=False)
    file_name = models.TextField(100,null=False)
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(30,null=False)
    source_archive = models.TextField(30,null=False)
    location_type = models.TextField(8,null=False)
    timemark = models.DateTimeField(null=False)
    begin_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    ingested = models.BooleanField(null=False)

# Model for station metadata downloaded by Jeff's script
class gauge_station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.TextField(20,null=False) # (original station value, which is a text field )
    lat = models.FloatField() # ?
    lon = models.FloatField() # ?
    tz = models.TextField(8,null=False)
    gauge_owner = models.TextField(200,null=False) 
    location_name = models.TextField(200,null=False) 
    location_type = models.TextField(8,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    apsviz_station = models.BooleanField(null=True)
    geom = models.PointField(null=False)

    class Meta:
        indexes = [models.Index(fields=['station_id', 'station_name', 'geom']),]

# Model for station metadata downloaded by Jeff's script
class apsviz_station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.TextField(20,null=False) # (original station value, which is a text field )
    lat = models.FloatField() # ?
    lon = models.FloatField() # ?
    location_name = models.TextField(30,null=False)
    tz = models.TextField(8,null=False)
    gauge_owner = models.TextField(30,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)
    timemark = models.DateTimeField(null=False)
    model_run_id = models.TextField(40,null=True)
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(30,null=False)
    source_instance = models.TextField(35,null=False)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    forcing_metaclass = models.TextField(15,null=False)
    location_type = models.TextField(8,null=False)
    grid_name = models.TextField(30,null=False)
    csvurl =  models.TextField(100,null=True)
    
    class Meta:
        indexes = [models.Index(fields=['station_id', 'station_name', 'geom']),]

# Model for station metadata downloaded by Jeff's script
class retain_obs_station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.TextField(20,null=False) # (original station value, which is a text field )
    lat = models.FloatField() # ?
    lon = models.FloatField() # ?
    location_name = models.TextField(30,null=False)
    tz = models.TextField(8,null=False)
    gauge_owner = models.TextField(30,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)
    timemark = models.DateTimeField(null=False)
    begin_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    data_source = models.TextField(200,null=False)
    source_name = models.TextField(30,null=False)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    location_type = models.TextField(8,null=False)

    class Meta:
        indexes = [models.Index(fields=['station_id', 'station_name', 'geom']),]

# Model for gauge source data, including ADCIRC data 
class gauge_source(models.Model):
    source_id = models.AutoField(primary_key=True)
    station_id = models.IntegerField()
    data_source = models.TextField(200,null=False) # (grid names such as hsofs_0, and just gauge) THINK ABOUT TYPE!
    source_name = models.TextField(20,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    units = models.TextField(10,null=True)

    class Meta:
        indexes = [models.Index(fields=['source_id', 'station_id', 'data_source']),]

# Model for data data downloaded by harvest scripts
class gauge_data(models.Model):
    obs_id = models.AutoField(primary_key=True)
    source_id = models.IntegerField()
    timemark = models.DateTimeField(null=False)
    time =  TimescaleDateTimeField(interval="10 day")
    water_level = models.FloatField(null=True)
    wave_height = models.FloatField(null=True)
    wind_speed = models.FloatField(null=True)
    air_pressure = models.FloatField(null=True)
    stream_elevation = models.FloatField(null=True)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        indexes = [models.Index(fields=['obs_id', 'source_id', 'water_level', 'timemark']),]
 
# Model for combined view of gauge_station, gauge_source and gauge_data
class gauge_station_source_data(models.Model):
    obs_id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    station_id = models.IntegerField()
    station_name = models.TextField(20,null=False)
    timemark = models.DateTimeField(null=True)
    time =  TimescaleDateTimeField(interval="10 day")
    water_level = models.FloatField(null=True)
    wave_height = models.FloatField(null=True)    
    wind_speed = models.FloatField(null=True)
    air_pressure = models.FloatField(null=True)
    stream_elevation = models.FloatField(null=True)
    tz = models.TextField(8,null=False)
    units = models.TextField(10,null=True)
    gauge_owner = models.TextField(200,null=False) # (noaa, ncem, usgs...)
    data_source = models.TextField(200,null=False) # (grid names such as hsofs_0, and just gauge) THINK ABOUT TYPE!
    source_name = models.TextField(20,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    location_name = models.TextField(200,null=False) # (name from noaa and contrails)
    location_type = models.TextField(8,null=False)
    apsviz_station = models.BooleanField(null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_gauge_station_source_data"

# Model for ADCIRC model source data
class model_source(models.Model):
    source_id = models.AutoField(primary_key=True)
    station_id = models.IntegerField()
    data_source = models.TextField(50,null=False) # (grid names such as hsofs_0, and just gauge) THINK ABOUT TYPE!
    source_instance = models.TextField(35,null=False)
    source_name = models.TextField(20,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    forcing_metaclass = models.TextField(15,null=False)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    units = models.TextField(10,null=True)

    class Meta:
        indexes = [models.Index(fields=['source_id', 'station_id', 'data_source']),]

# Model for ADCIRC model data generated by harvest scripts
class model_data(models.Model):
    model_id = models.AutoField(primary_key=True)
    source_id = models.IntegerField()
    timemark = models.DateTimeField(null=False)
    time =  TimescaleDateTimeField(interval="10 day")
    water_level = models.FloatField(null=True)
    wave_height = models.FloatField(null=True)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        indexes = [models.Index(fields=['model_id', 'source_id', 'water_level', 'timemark']),]

# Model for combined view of gauge_station, gauge_source and gauge_data
class model_station_source_data(models.Model):
    model_id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    station_id = models.IntegerField()
    station_name = models.TextField(20,null=False)
    timemark = models.DateTimeField(null=True)
    time =  TimescaleDateTimeField(interval="10 day")
    model_run_id = models.TextField(35,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    water_level = models.FloatField(null=True)
    wave_height = models.FloatField(null=True)
    tz = models.TextField(8,null=False)
    units = models.TextField(10,null=True)
    gauge_owner = models.TextField(200,null=False) # (noaa, ncem, usgs...)
    data_source = models.TextField(200,null=False) # (grid names such as hsofs_0, and just gauge) THINK ABOUT TYPE!
    source_name = models.TextField(20,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    source_instance = models.TextField(35,null=False)
    forcing_metaclass = models.TextField(15,null=False)
    location_name = models.TextField(200,null=False) # (name from noaa and contrails)
    location_type = models.TextField(8,null=False)
    apsviz_station = models.BooleanField(null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_model_station_source_data"
