from django.apps import AppConfig


class BlogConfig(AppConfig): # go to settings and add path
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
