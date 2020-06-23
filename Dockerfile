FROM python:3 as backendbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt
COPY . /code/

EXPOSE 8888
#STOPSIGNAL SIGTERM

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/bin/bash","./entrypoint.sh"]
