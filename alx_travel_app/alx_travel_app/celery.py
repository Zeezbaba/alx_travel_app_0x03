# import os
# from celery import Celery
# from dotenv import load_dotenv

# load_dotenv()  # Loads variables from .env

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# app = Celery('alx_travel_app')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()

from __future__ import absolute_import
import os
from celery import Celery

# Set the default Django settings module for 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

# Load settings from Django settings using CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')