# Database Snapshot 

[![Github Build](https://github.com/Geoluminate/geoluminate-db-snapshot/actions/workflows/build.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-db-snapshot/actions/workflows/build.yml)
[![Github Docs](https://github.com/Geoluminate/geoluminate-db-snapshot/actions/workflows/docs.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-db-snapshot/actions/workflows/docs.yml)
[![CodeCov](https://codecov.io/gh/Geoluminate/geoluminate-db-snapshot/branch/main/graph/badge.svg?token=0Q18CLIKZE)](https://codecov.io/gh/Geoluminate/geoluminate-db-snapshot)
![GitHub](https://img.shields.io/github/license/Geoluminate/geoluminate-db-snapshot)
![GitHub last commit](https://img.shields.io/github/last-commit/Geoluminate/geoluminate-db-snapshot)
![PyPI](https://img.shields.io/pypi/v/geoluminate-db-snapshot)
<!-- [![RTD](https://readthedocs.org/projects/geoluminate-db-snapshot/badge/?version=latest)](https://geoluminate-db-snapshot.readthedocs.io/en/latest/readme.html) -->
<!-- [![Documentation](https://github.com/Geoluminate/geoluminate-db-snapshot/actions/workflows/build-docs.yml/badge.svg)](https://github.com/Geoluminate/geoluminate-db-snapshot/actions/workflows/build-docs.yml) -->
<!-- [![PR](https://img.shields.io/github/issues-pr/Geoluminate/geoluminate-db-snapshot)](https://github.com/Geoluminate/geoluminate-db-snapshot/pulls)
[![Issues](https://img.shields.io/github/issues-raw/Geoluminate/geoluminate-db-snapshot)](https://github.com/Geoluminate/geoluminate-db-snapshot/pulls) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/geoluminate-db-snapshot) -->
<!-- ![PyPI - Status](https://img.shields.io/pypi/status/geoluminate-db-snapshot) -->

A scientific db_snapshot management app for Django

Documentation
-------------

The full documentation is at https://ssjenny90.github.io/geoluminate-db-snapshot/

Quickstart
----------

Install Database Snapshot::

    pip install geoluminate-db-snapshot

Add it to your `INSTALLED_APPS`:


    INSTALLED_APPS = (
        ...
        'db_snapshot',
        ...
    )

Add Database Snapshot's URL patterns:

    urlpatterns = [
        ...
        path('', include("db_snapshot.urls")),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

