###########
# BUILDER #
###########

# pull official base image
FROM python:3.9 as builder

# set work directory
WORKDIR /usr/src/django

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update 

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
RUN flake8 --ignore=E501,F401 ./apsviz_gauges

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/django/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9

# create directory for the django user
RUN mkdir -p /home/django

# create the django user
RUN groupadd -r -g 1001 django && useradd --no-log-init -r -u 1001 -g 1001 django

# create the appropriate directories
ENV HOME=/home/django
ENV DJANGO_HOME=/home/django/web
RUN mkdir $DJANGO_HOME
RUN mkdir $DJANGO_HOME/staticfiles
RUN mkdir $DJANGO_HOME/mediafiles
WORKDIR $DJANGO_HOME

# install dependencies
RUN apt-get update && apt-get install -y \
  netcat \
  binutils \
  libproj-dev \
  gdal-bin \
  postgresql-client

COPY --from=builder /usr/src/django/wheels /wheels
COPY --from=builder /usr/src/django/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh $DJANGO_HOME

# copy project
COPY . $DJANGO_HOME

# chown all the files to the django user
RUN chown -R django:django $DJANGO_HOME

# change to the django user
USER django 

# run entrypoint.sh
ENTRYPOINT ["/home/django/web/entrypoint.sh"]
