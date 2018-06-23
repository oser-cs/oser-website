from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'
    verbose_name = 'Projets'

    def ready(self):
        from . import signals
