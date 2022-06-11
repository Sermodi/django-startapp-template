from django.apps import AppConfig


class {{ camel_case_app_name }}(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ app_name}}'
