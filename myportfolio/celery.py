from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULES', 'myportfolio.settings')
app = Celery('myportfolio')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.broker_url = "redis://default:kQCInXrffQcYwrezWqnfnGJzfLEVRjmc@viaduct.proxy.rlwy.net:35323"
app.conf.result_backend = "redis://default:kQCInXrffQcYwrezWqnfnGJzfLEVRjmc@viaduct.proxy.rlwy.net:35323"
app.conf.task_track_started = True
app.conf.task_time_limit = 30 * 60
app.conf.worker_prefetch_multiplier = 1
app.conf.broker_connection_retry_on_startup = True
app.conf.timezone = 'Africa/Lagos'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')