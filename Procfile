web: gunicorn --pythonpath bowls bowls.wsgi -b 0.0.0.0:$PORT
#web: uwsgi --chdir=$HOME/bowls --reaper --vacuum --master --processes 8 --single-interpreter --enable-threads --http-socket=0.0.0.0:$PORT --uid=stackato --gid=stackato --static-map /static=$HOME/bowls/staticfiles bowls/wsgi.py
