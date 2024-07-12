from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_api_project_folder.settings')

app = Celery('drf_api_project_folder')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')



app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")