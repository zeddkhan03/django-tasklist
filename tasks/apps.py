from django.apps import AppConfig

# app registered according to it's name
class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
