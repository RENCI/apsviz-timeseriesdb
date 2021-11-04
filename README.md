# apsviz-timeseriesdb
This repository contains the software for creating a Django Rest Framework application that serves gauge observation data from postgresql/timescaledb/postgis database.

# Development 

## Build docker images and containers for the backend

After downloading or cloning the repository, change your directory to the project root directory:

cd apsviz-timeseriesdb

In the project root directory create a file named .env.dev and add the following information to it:

DEBUG=1  
SECRET_KEY=change_me  
DJANGO_ALLOWED_HOSTS=localhost 0.0.0.0 127.0.0.1 [::1]  
SQL_ENGINE=timescale.db.backends.postgis  
SQL_DATABASE=apsviz_gauges  
SQL_USER=apsviz_gauges  
SQL_PASSWORD=xxxxxxxxx  
SQL_HOST=db  
SQL_PORT=5432  
DATABASE=postgres  

Add your own password.

In the next step, from the project root directory run docker-compose on the development docker-compose.yml file:

docker-compose up -d --build

After this process has finished run "python manage.py collectstatic" using the docker-compose command:

docker-compose exec web python manage.py collectstatic --no-input --clear

Then run "python manage.py makemigrations" using the docker-compose command:

docker-compose exec web python manage.py makemigrations --noinput

The run "python manage.py migrate" using the docker-compose command:

docker-compose exec web python manage.py migrate --no-input

At this poing the database is ready for ingest of data.

