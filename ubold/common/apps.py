from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = "ubold.common"
    verbose_name = "Common"

    def ready(self):
        pass
