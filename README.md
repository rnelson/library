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

Once you've cloned this repo, create a new file `library/override_settings.py`. 
This file, if it exists, will be loaded by the standard settings file and is 
used to override other settings.

At present, the default settings are tailored to production rather than 
development (I'll fix that at some point), so you'll need to fix static files 
using `override_settings.py`:

```
from library.settings import BASE_DIR
import os

STATIC_ROOT = ''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

Once that's done, simply run `python manage.py runserver` and you can access 
your local instance.

## Production

This is a shortened version of what I did to deploy.

1. `mkdir /srv/library`
2. `virtualenv /srv/library/env`
3. `source /srv/library/env/bin/activate`
4. `git clone (url) /srv/library/app`
5. `(cd /srv/library/app && pip install -r requirements.txt)`
6. `/srv/library/env/bin/gunicorn -c /srv/library/gunicorn_config.py library.wsgi:application`

My `/srv/library/gunicorn_config.py` looks like this:

```
command = '/srv/library/env/bin/gunicorn'
pythonpath = '/srv/library/app'
bind = '127.0.0.1:8001'
workers = 3
```

## License

Released under the [MIT License](http://rnelson.mit-license.org).


