# Django Boiler Plate

## Features
1. django-allauth
    - Signin, Signup, Password Reset, Multiple Email Addresses and more.
2. google social login
3. celery, beat, redis
4. [Nice Admin Dashboard Template](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/)
5. Docker and docker-compose
6. PostgreSQL
7. [htmx.org](https://htmx.org/)
8. djmail to send emails using celery
9. django_db_logger for logging to the database.
10. Custom template tags, management commands
11. i18n supporting English and Turkish
12. Email sending for email verification.
13. Bootstrap 5, ChartJS


## Installations

```bash
# clone the project
git clone https://github.com/adnankaya/djbp.git
# go to project directory
cd djbp
# create venv instance named as env
python3 -m venv env
# for linux/macos users
source env/bin/activate
# for windows users
.\env\Scripts\activate
# install packages
pip install -r requirements.txt
# .env file creation
cp .env.example .env
# Migrate files
python manage.py migrate
# [Optional] make migrations if necessary
python manage.py makemigrations app-name
python manage.py migrate
# [DEVELOPMENT] init all command
python manage.py init_all
# run project for development mode
python manage.py runserver --settings=src.settings.dev
# run project for production mode
python manage.py runserver --settings=src.settings.prod
# run project for test mode
python manage.py runserver --settings=src.settings.settings_for_test
```
## Static Files
```
python manage.py collectstatic
```

## Internationalization
```
python manage.py makemessages -l tr --ignore=venv
python manage.py compilemessages
```

---

## Technical Notes

1. Find and remove migration files
```bash
find . -path "*/migrations/*.py" -not -path "./venv/*" -not -name "__init__.py" -delete
```

## Load Test
```bash
# run gunicorn with 4 workers
gunicorn core.wsgi:application -w 4

# new terminal apache bench
ab -n 100 -c 10 http://127.0.0.1:8000/
# This will simulate 100 connections over 10 concurrent threads. That's 100 requests, 10 at a time.
```

#### Debugging Celery tasks
- Dockerfile
```bash
# install system dependencies
RUN apt-get update && apt-get install -y telnet
```
- python side
```python
# tasks.py

from celery.contrib import rdb

def mytask():
    # ...
    rdb.set_trace()
    # ...
```
0. Trigger related celery task
1. `docker compose exec worker bash`
2. `root@fc4dcaa377b1:/usr/src/app# telnet 0.0.0.0 6900`

#### Remove Docker none tag images
```bash
docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi
```