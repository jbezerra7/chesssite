from django.apps import AppConfig


class ChessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chess'
    
    def ready(self):
        from . import signals