#!/bin/bash

source ../.env.db

PGPASSWORD=$POSTGRES_PASSWORD psql -U apsviz_gauges -d apsviz_gauges -p 5432 -h localhost -f ingest_dbo_GAGES_ALL.sql
PGPASSWORD=$POSTGRES_PASSWORD psql -U apsviz_gauges -d apsviz_gauges -p 5432 -h localhost -f ingest_noaa_stations.sql
PGPASSWORD=$POSTGRES_PASSWORD psql -U apsviz_gauges -d apsviz_gauges -p 5432 -h localhost -f ingest_ndbc_stations.sql
