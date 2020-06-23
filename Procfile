web: gunicorn django_dramatiq_example.wsgi --log-file -
worker: python manage.py rundramatiq -p4 -t4
