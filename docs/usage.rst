=====
Usage
=====

To use Database Snapshot in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'db_snapshot.apps.GlossaryConfig',
        ...
    )

Add Database Snapshot's URL patterns:

.. code-block:: python

    from db_snapshot import urls as db_snapshot_urls


    urlpatterns = [
        ...
        url(r'^', include(db_snapshot_urls)),
        ...
    ]
