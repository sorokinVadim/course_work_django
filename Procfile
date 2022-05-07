celery-worker:
    celery -A course_work worker -l INFO -f celery_worker.log
celery-beat:
    celery -A course_work beat -l INFO -f celery_beat.log
web:
    python manage.py runserver
