from celery import shared_task
from .models import Item
from datetime import date


@shared_task(name="update_items")
def update_items():
    items = Item.objects.all()
    for item in items:
        if item.save_until < date.today():
            item.owner = None
            item.save()
