COPY noaa_stations(tidal,greatlakes,shefcode,state,timezone,timezonecorr,observedst,stormsurge,forecast,nonNavigational,station_name,name,lat,lon,affiliations,portscode,self,expand,tideType,details,sensors,floodlevels,datums,supersededdatums,harmonicConstituents,benchmarks,tidePredOffsets,nearby,products,disclaimers,notices)
FROM '/home/noaa_stations.csv'
DELIMITER ','
CSV HEADER;
