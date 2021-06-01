FROM python:3.8

ENV DJANGO_SETTINGS_MODULE bowls.settings.production
WORKDIR /var/app

COPY requirements/ requirements
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY app/ /var/app

RUN python manage.py collectstatic

EXPOSE 8000
ENTRYPOINT ["gunicorn", "bowls:wsgi", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000"]