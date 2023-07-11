# __init__.py

# Importar la aplicación de Celery
from .celery import app as celery_app

# Configurar la aplicación de Celery como la aplicación por defecto para tareas
__all__ = ('celery_app',)
