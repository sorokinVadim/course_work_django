celery -A course_work worker -l INFO -f celery_worker.log | celery -A course_work beat -l INFO -f celery_beat.log
