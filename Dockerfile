FROM python:3.8

ADD . /opt/kinotake
WORKDIR /opt/kinotake

RUN pip install django psycopg2-binary

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
