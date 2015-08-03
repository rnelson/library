# Library

## About

This simple library app is meant to help me keep an updated list of things I 
own, particular board/card games. It doesn't have a ton of features, but it 
does what I need well enough.

## Requirements

+ [Django](http://djangoproject.com) 1.8.3
+ [django-admin-bootstrapped](https://pypi.python.org/pypi/django-admin-bootstrapped/2.5.4) 2.5.4
+ [django-bootstrap3](https://pypi.python.org/pypi/django-bootstrap3/6.1.0) 6.1.0
+ [gunicorn](http://gunicorn.org) 19.3.0

## Development

Once you've cloned this repo, simply run `python manage.py runserver` and you 
can access your local instance. The database will be a local SQLite file.

## Production

This is a shortened version of what I did to deploy.

1. `mkdir /srv/library`
2. `virtualenv /srv/library/env`
3. `source /srv/library/env/bin/activate`
4. `git clone (url) /srv/library/app`
5. `(cd /srv/library/app && pip install -r requirements.txt)`
6. (`override_settings` and database stuff; see below)
7. `python manage.py migrate`
8. `python manage.py createsuperuser`
9. `/srv/library/env/bin/gunicorn -c /srv/library/gunicorn_config.py library.wsgi:application`

My `/srv/library/gunicorn_config.py` looks like this:

```
command = '/srv/library/env/bin/gunicorn'
pythonpath = '/srv/library/app'
bind = '127.0.0.1:8001'
workers = 3
```

I bind to port 8001 because [the site sits behind nginx](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps#step-four-configure-your-vps).

You will also need an `override_settings.py` file (lives in `app/library/settings`, 
but I created a symlink there to a file outside of the repo so I can re-clone 
later if needed). Here's an example:

```
import os
from library.settings import BASE_DIR

SECRET_KEY = 'my super secret key that differs from development'
DEBUG = False
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mylibrary',
        'USER': 'mylibraryuser',
        'PASSWORD': 'mylibrarypass',
        'HOST': 'localhost',
        'POST': '',
    }
}
```

Obviously, set a secret key that is actually a secret and configure the 
database to your liking. I run PostgreSQL on the machine so I simply created a 
user and a database owned by that user and the migration set everything up for 
me. You can use any database backend that is supported, or simply don't touch 
`DATABASES` to continue using a SQLite file on the filesystem.

## License

Released under the [MIT License](http://rnelson.mit-license.org).


