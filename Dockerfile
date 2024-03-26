# pull official base image
FROM --platform=linux/amd64 python:3.11.0-slim-buster

ENV APP_HOME=/usr/src/app
RUN mkdir $APP_HOME
# set work directory
WORKDIR $APP_HOME
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat telnet

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

# run entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint"]