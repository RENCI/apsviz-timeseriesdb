COPY ndbc_stations(station,lat,lon,name,units,tz,owner,state,county)
FROM '/home/ndbc_stations.csv'
DELIMITER ','
CSV HEADER;
