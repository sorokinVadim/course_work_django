from .models import *

def get_text(client: Client, item: Item):
    code = f"{client.passport_num:08d}:{client.id}:{item.id}"
    return \
        f"""# {code}
## Ім'я: {client.first_name} {client.last_name}
## Найменування предмету: {item.name}
- Оціночна вартість: {item.estimated_cost}
- Сума, видана під заставу: {item.amount_pledged}
- Зберігається до: {item.save_until}
"""
