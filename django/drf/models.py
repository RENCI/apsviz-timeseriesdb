from __future__ import unicode_literals
from django.contrib.gis.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

# Model for station metadata downloaded by Jeff's script
class gauge_stations(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.TextField(20,null=False)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.TextField(200,null=False)
    units = models.TextField(10,null=False)
    tz = models.TextField(8,null=False)
    owner = models.TextField(20,null=False)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

# Model for observation data downloaded by Jeff's script
class gauge_observations(models.Model):
    id = models.AutoField(primary_key=True)
    time =  TimescaleDateTimeField(interval="1 day")
    station = models.TextField(20,null=False)
    water_level = models.FloatField(null=True)

# Model for combined view of gauge_station and gauge_observations
class gauge_stations_observations(models.Model):
    id = models.AutoField(primary_key=True)
    station = models.TextField(20,null=False)
    time =  TimescaleDateTimeField(interval="1 day")
    water_level = models.FloatField(null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.TextField(200,null=False)
    units = models.TextField(10,null=False)
    tz = models.TextField(8,null=False)
    owner = models.TextField(20,null=False)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_gauge_stations_observations"

# Model for FIMAN gauge geometries.
class nc_gauge_geom(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.TextField(20,null=False)
    county = models.TextField(20,null=False)
    name = models.TextField(50,null=False)
    owner = models.TextField(10,null=False)
    rain_only_gage = models.FloatField(null=True)
    in_service = models.IntegerField()
    is_coastal = models.IntegerField()
    geom = models.PointField(null=False)

# Model for FIMAN gauge data.
class nc_gauge_data(models.Model):
    id = models.AutoField(primary_key=True)
    data_time = TimescaleDateTimeField(interval="1 day")
    site_id = models.TextField(20,null=False)
    sensor_id = models.TextField(10,null=False)
    or_site_id = models.IntegerField()
    or_sensor_id = models.IntegerField()
    sensor_class = models.IntegerField()
    receive_time = models.DateTimeField(null=False)
    data_value = models.FloatField(null=True)
    raw_value = models.FloatField(null=True)
    data_quality = models.TextField(5,null=False)
    units = models.TextField(5,null=False)

# Model view for FIMAN gauge data and geometries
class nc_gauge_data_geom(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.TextField(20,null=False)
    sensor_id = models.TextField(10,null=False)
    or_site_id = models.IntegerField()
    or_sensor_id = models.IntegerField()
    sensor_class = models.IntegerField()
    receive_time = models.DateTimeField(null=False)
    data_time = TimescaleDateTimeField(interval="1 day")
    data_value = models.FloatField(null=True)
    raw_value = models.FloatField(null=True)
    data_quality = models.TextField(5,null=False)
    units = models.TextField(5,null=False)
    county = models.TextField(20,null=False)
    name = models.TextField(50,null=False)
    owner = models.TextField(10,null=False)
    rain_only_gage = models.FloatField(null=True)
    in_service = models.IntegerField()
    is_coastal = models.IntegerField()
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_nc_gauge_data_geom"

# Model for NOAA gauge geometries
class noaa_gauge_geom(models.Model):
    id = models.AutoField(primary_key=True)
    stationid = models.IntegerField()
    gauge_name = models.TextField(20,null=False)
    geom = models.PointField(null=False)

# Model for NOAA gauge data
class noaa_gauge_data(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = TimescaleDateTimeField(interval="1 day")
    water_level = models.FloatField(null=True)
    sigma = models.FloatField(null=True)
    flags = models.TextField(20,null=False)
    qc = models.TextField(5,null=False)
    provider = models.TextField(10,null=False)
    stationid = models.IntegerField()
    datatype = models.TextField(20,null=False)
    vertdatum = models.TextField(5,null=False)

# Model view for NOAA gauge data and geometries
class noaa_gauge_data_geom(models.Model):
    id = models.IntegerField(primary_key=True)
    gauge_name = models.TextField(20,null=False)
    date_time = TimescaleDateTimeField(interval="1 day")
    water_level = models.FloatField(null=True)
    sigma = models.FloatField(null=True)
    flags = models.TextField(20,null=False)
    qc = models.TextField(5,null=False)
    provider = models.TextField(10,null=False)
    stationid = models.IntegerField()
    datatype = models.TextField(20,null=False)
    vertdatum = models.TextField(5,null=False)
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_noaa_gauge_data_geom"

