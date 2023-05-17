from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from simple_menu import Menu, MenuItem

Menu.add_item(
    "toolbar",
    MenuItem(
        _("Snapshots"),
        reverse("db_snapshot"),
        weight=6,
        icon="fa-history",
    ),
)
