FROM python:3 as backendbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
#RUN git --version
#RUN python -m venv venv
#RUN /bin/bash source venv/bin/activate
#RUN python -m pip install --upgrade pip
RUN pip install -r req.txt
#RUN pip uninstall -y cryptography
#RUN pip install cryptography

COPY . /code/
#RUN chmod +x ./entrypoint.sh
#ENV MYSQL_HOST=172.17.0.1
#ENV MYSQL_USER="root"
#ENV MYSQL_PASS="123"
#ENV MYSQL_NAME="3wappv2"

EXPOSE 8888

#CMD ["gunicorn", "-w 4","--bind", "0.0.0.0:8000", "app.wsgi"]
#CMD ["celery", "-A", "app", "worker", "-S", "django" "-l", "info"]

# celery -A app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#CMD ["celery", "-A", "app", "beat", "-l", "info" "--scheduler", "django_celery_beat.schedulers:DatabaseScheduler"]
#STOPSIGNAL SIGTERM
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/bin/bash","./entrypoint.sh"]