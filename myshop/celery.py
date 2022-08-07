import os
from celery import Celery

# set the default Django celery module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

broker_url = 'amqp://guest:guest@127.0.0.1:5672/myvhost'

app = Celery('myshop', broker=broker_url)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()