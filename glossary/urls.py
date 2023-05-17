from django.urls import path

from .views import SnapshotView

urlpatterns = [
    path("snapshots/", SnapshotView.as_view(), name="db_snapshot"),
]
