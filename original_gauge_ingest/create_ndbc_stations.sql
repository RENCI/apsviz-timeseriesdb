CREATE TABLE IF NOT EXISTS ndbc_stations (
   ID SERIAL PRIMARY KEY,
   station VARCHAR (5) NOT NULL,
   lat FLOAT NOT NULL,
   lon FLOAT NOT NULL,
   name VARCHAR (50) NOT NULL,
   units VARCHAR (2) NOT NULL,
   tz VARCHAR (3) NOT NULL,
   owner VARCHAR (4) NULL,
   state VARCHAR (4) NULL,
   county VARCHAR (4) NULL
);
