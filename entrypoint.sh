#!/bin/bash
#MYSQL_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')
#DOCKER_HOST=$(ip route show default | awk '/default/ {print $3}')
#DOCKER_HOST=$(/sbin/ip route | awk '/default/ { print $3 }')
#echo "DOCKER HOST: ${DOCKER_HOST}"
#export MYSQL_HOST=$(echo $DOCKER_HOST)
#echo "MYSQL HOST: ${MYSQL_HOST}"
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

#echo "Starting celery services.."
#echo "starting celery workers"

#celery -A app worker -S django -l info -c 2 --pool=gevent &
# celery -A app worker -S django -l debug --pool=solo
#echo "starting celery task scheduler"
#celery -A app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
# celery -A app beat -l debug --scheduler django_celery_beat.schedulers:DatabaseScheduler &

#echo "Starting Dev Mail Server..."
#python -m smtpd -n -c DebuggingServer localhost:1025 &

#BACKEND_HOST="${BACKEND_HOST:-0.0.0.0}"
#BACKEND_PORT="${BACKEND_PORT:-8000}"

#echo "Starting dvelopment Server"
#python manage.py runserver 0.0.0.0:${BACKEND_PORT}
#gunicorn --bind $BACKEND_HOST:$BACKEND_PORT app.wsgi

python manage.py rundramatiq -p4 -t4 &

gunicorn -c /code/gunicorn_config.py django_dramatiq_example.wsgi

