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
    station_id = models.AutoField(primary_key=True)
    station_location_id = models.TextField(20,null=False)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.TextField(200,null=False)
    units = models.TextField(10,null=False)
    tz = models.TextField(8,null=False)
    owner = models.TextField(20,null=False)
    source_archive = models.TextField(20,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

# Model for observation data downloaded by Jeff's script
class gauge_observations(models.Model):
    obs_id = models.AutoField(primary_key=True)
    station_id = models.IntegerField()
    station_location_id = models.TextField(20,null=False)
    time =  TimescaleDateTimeField(interval="1 day")
    water_level = models.FloatField(null=True)

# Model for combined view of gauge_station and gauge_observations
class gauge_stations_observations(models.Model):
    obs_id = models.IntegerField(primary_key=True)
    station_id = models.IntegerField() 
    station_location_id = models.TextField(20,null=False)
    time =  TimescaleDateTimeField(interval="1 day")
    water_level = models.FloatField(null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.TextField(200,null=False)
    units = models.TextField(10,null=False)
    tz = models.TextField(8,null=False)
    owner = models.TextField(20,null=False)
    source_archive = models.TextField(20,null=False)
    country = models.TextField(20,null=True)
    state = models.TextField(20,null=True)
    county = models.TextField(20,null=True)
    geom = models.PointField(null=False)

    objects = models.Manager()
    timescale = TimescaleManager()

    class Meta:
        managed = False
        db_table = "drf_gauge_stations_observations"

