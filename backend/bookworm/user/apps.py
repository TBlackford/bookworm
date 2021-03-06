from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookworm.user'
    label = 'bookworm_user'

    def ready(self):
        from bookworm.user.data import models
