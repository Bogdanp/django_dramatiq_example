#!/bin/bash
# This is to make sure it only runs the first time the container is starting.
# no need to do migration if the code did not change.
FILE=/code/installed.txt
if [[ -f "$FILE" ]]; then
    echo "$FILE exists. starting server"
else
	echo "Making Migrations..."
	python manage.py makemigrations
	echo "Running Migrations..."
	python manage.py migrate
	echo "collecting static files"
	python manage.py collectstatic --noinput
	touch $FILE
fi

echo "starting workers workers"
python manage.py rundramatiq -p4 -t4 &

echo "Starting app with gunicorn...."
gunicorn -c /code/gunicorn_config.py django_dramatiq_example.wsgi

