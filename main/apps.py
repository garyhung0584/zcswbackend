from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
<<<<<<< HEAD
    
    def ready(self):
        import main.signals
=======

    def ready(self):
        import main.signals
>>>>>>> 021a895 (希望這樣是對的)
