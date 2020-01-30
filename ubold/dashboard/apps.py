from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = "ubold.dashboard"
    verbose_name = "Dashboard"

    def ready(self):
        pass
