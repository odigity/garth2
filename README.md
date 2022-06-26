## Changelog

```
~/src                $ django-admin startproject garth2
~/src                $ cd garth2
~/src/garth2         $ git init .

~/src/garth2         $ mkdir tests
~/src/garth2         $ touch tests/__init__.py

~/src/garth2         $ nano manage.py

    python  ->  python3

~/src/garth2         $ mv garth2/ tmp
~/src/garth2         $ ./manage.py startapp garth2
~/src/garth2         $ mv tmp garth2/config
~/src/garth2         $ nano manage.py

    DJANGO...MODULE  : garth2.settings  ->  garth2.config.settings

~/src/garth2         $ cd garth2
~/src/garth2/garth2  $ nano config/settings.py

    BASE_DIR         : += `.parent`
    INSTALLED_APPS   : += 'garth2'
    ROOT_URLCONF     : garth2.urls              ->  garth2.config.urls
    WSGI_APPLICATION : garth2.wsgi.application  ->  garth2.config.wsgi.application

~/src/garth2/garth2  $ nano config/wsgi.py

    DJANGO...MODULE  : garth2.settings  ->  garth2.config.settings

~/src/garth2/garth2  $ rm admin.py models.py tests.py views.py config/asgi.py
~/src/garth2/garth2  $ mkdir models
~/src/garth2/garth2  $ nano models/thingy.py

    class Thingy(models.Model)
    class ThingyAdmin(admin.ModelAdmin)

~/src/garth2/garth2  $ nano models/__init__.py

    from .thingy import Thingy

~/src/garth2/garth2  $ cd ..
~/src/garth2         $ ./manage.py makemigrations
```

### Also...

- configured [django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/)
- configured [django-extensions](https://pypi.org/project/django-extensions/)
- configured SQL logging as in https://neilwithdata.com/django-sql-logging

## Current State

```
~/src/garth2  $ tree
.
├── garth2
│   ├── apps.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   └── models
│       ├── __init__.py
│       └── thingy.py
├── manage.py
├── README.md
├── requirements.txt
└── tests
    └── __init__.py
```
