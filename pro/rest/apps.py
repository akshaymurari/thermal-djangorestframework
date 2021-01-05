from django.apps import AppConfig


class RestConfig(AppConfig):
    name = 'rest'
    def ready(self):
        import rest.signals