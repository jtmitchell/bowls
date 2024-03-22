web: gunicorn --pythonpath bowls config.wsgi
release: ./bowls/manage.py migrate --noinput
worker: celery -A config worker --time-limit=300 -O fair
beat: celery -A config beat
