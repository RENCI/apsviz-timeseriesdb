from __future__ import unicode_literals
from django.contrib.gis.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

# Model for input gauge data files
class gauge_data_file(models.Model):
    file_id = models.AutoField(primary_key=True)
    dir_path = models.TextField(100,null=False)
    file_name = models.TextField(100,null=False)
    data_date_time = models.DateTimeField(null=True) 
    data_begin_time = models.DateTimeField(null=True)
    data_end_time = models.DateTimeField(null=True)
    file_date_time = models.DateTimeField(null=True)
    source = models.TextField(30,null=False)
    content_info = models.TextField(30,null=False)
    ingested = models.BooleanField(null=False)
 
# Model for station metadata downloaded by Jeff's script
class gauge_station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.TextField(20,null=False) # (original station value, which is a text field )
    lat = models.FloatField() # ?
    lon = models.FloatField() # ?
    tz = models.TextField(8,null=False)
    gauge_owner = models.TextField(200,null=False) # (noaa, ncem, usgs...)
    location_name = models.TextField(200,null=False) # (name from noaa and contrails)
    location_type = models.TextField(8,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

# Model for gauge source data, including ADCIRC data 
class gauge_source(models.Model):
    source_id = models.AutoField(primary_key=True)
    #station_id = models.ForeignKey(gauge_station, on_delete=models.CASCADE) # DO I HAVE TO SPECIFY station_id? NEED TO COME BACK TO THIS.
    station_id = models.IntegerField()
    data_source = models.TextField(200,null=False) # (grid names such as hsofs_0, and just gauge) THINK ABOUT TYPE!
    source_name = models.TextField(20,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)

# Model for data data downloaded by harvest scripts
class gauge_data(models.Model):
    obs_id = models.AutoField(primary_key=True)
    #source_id = models.ForeignKey(gauge_source, on_delete=models.CASCADE) # ?? NEED TO COME BACK TO THIS.
    source_id = models.IntegerField()
    timemark = models.DateTimeField(null=False)
    time =  TimescaleDateTimeField(interval="10 day")
    water_level = models.FloatField(null=True)
 
# Model for combined view of gauge_station, gauge_source and gauge_data
class gauge_station_source_data(models.Model):
    obs_id = models.IntegerField(primary_key=True)
    #source_id = models.ForeignKey(gauge_source, on_delete=models.CASCADE) # NEED TO COME BACK TO THIS.
    source_id = models.IntegerField()
    #station_id = models.ForeignKey(gauge_station, on_delete=models.CASCADE) # NEED TO COME BACK TO THIS.
    station_id = models.IntegerField()
    station_name = models.TextField(20,null=False)
    timemark = models.DateTimeField(null=True)
    time =  TimescaleDateTimeField(interval="10 day")
    water_level = models.FloatField(null=True)
    tz = models.TextField(8,null=False)
    gauge_owner = models.TextField(200,null=False) # (noaa, ncem, usgs...)
    data_source = models.TextField(200,null=False) # (grid names such as hsofs_0, and just gauge) THINK ABOUT TYPE!
    source_name = models.TextField(20,null=False) # (noaa, ncem, adcirc_nowcast, adcirc_forecast?)
    source_archive = models.TextField(20,null=False) # (nomads?, contrails, renci, tacc..?)
    location_name = models.TextField(200,null=False) # (name from noaa and contrails)
    location_type = models.TextField(8,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_gauge_station_source_data"

