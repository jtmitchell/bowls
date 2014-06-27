bowls
=====

A django website to setup a lawn bowls tournament.

This project is cloud-friendly, and relies on environment variables to define the settings, and database.

When running from the commandline, 
* either use `DJANGO_SETTINGS_MODULE=bowls.settings.development`
* or add the settings to the manage command. `python manage.py validate --settings=bowls.settings.development`

`foreman` is also an option for running the app.
We already have a Procfile setup to run the app using gunicorn, so you just need to supply a .env file with
your settings, and start the app with `foreman start`

Sample .env
```
BOWLS_DB_USER=my-db-user
BOWLS_DB_PASSWORD=my-secret-password
DJANGO_SETTINGS_MODULE=bowls.settings.development
```
