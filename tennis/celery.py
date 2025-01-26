from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем настройки д ля Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

app = Celery('your_project')

# Настроим Celery для работы с настройками Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит все задачи в проектах
app.autodiscover_tasks()
