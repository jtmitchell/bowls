FROM python:3.11

ENV DJANGO_SETTINGS_MODULE bowls.settings.production
WORKDIR /var/app

COPY requirements.production.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY app/ /var/app

RUN python manage.py collectstatic

EXPOSE 8000
ENTRYPOINT ["gunicorn", "bowls:wsgi", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000"]
