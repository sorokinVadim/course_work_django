import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "course_work.settings")

app = Celery("course_work")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update_items": {
        "task": "update_items",
        "schedule": 60 * 60
    }
}

