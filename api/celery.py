import os
from celery import Celery

# Establece la variable de entorno para la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# Crea una instancia de la aplicación de Celery
app = Celery('api')

# Configuración de la aplicación de Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Buscar y carga las tareas de Celery desde todas las aplicaciones Django
app.autodiscover_tasks()
