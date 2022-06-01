from django.db.models import *
from django.urls import reverse


class Client(Model):
    first_name = CharField(max_length=30, verbose_name="И'мя")
    last_name = CharField(max_length=30, verbose_name="Прізвище")
    age = IntegerField(verbose_name="Вік")
    passport_num = IntegerField(verbose_name="Номер паспорта", unique=True)
    items: list = []

    def get_item(self, item_id: int):
        for item in self.items:
            if item.id == item_id:
                return item

    def get_absolute_url(self):
        return reverse('client', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('client-edit', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name}: {self.passport_num}'


class Item(Model):
    name = CharField(max_length=50, verbose_name="Найменування")
    estimated_cost = IntegerField(verbose_name="Оціночна вартість")
    amount_pledged = IntegerField(verbose_name="Сума, винная під заставу")
    date_make = DateField(auto_now_add=True, verbose_name="Дата сдачи")
    save_until = DateField(verbose_name="Зберігати до")
    owner = ForeignKey(Client, null=True, on_delete=SET_NULL, verbose_name="Власник")

    def get_absolute_url(self):
        return reverse('item', args=[str(self.id)])

    def get_edit_url(self):
        return reverse('item-edit', args=[str(self.id)])

    def get_consignment_url(self):
        return reverse('get_consignment', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Storage:
    def __init__(self, clients: list[Client], items: list[Item]):
        self.clients = clients
        self.items = items

    def get_clients(self, id=None, name=None):
        try:
            if id is not None:
                return list(filter(lambda c: c.id == id, self.clients))[0]
            elif name is not None:
                return filter(lambda c: c.name == name, self.clients)
            else:
                return None
        except:
            return None

    def add_clients(self, client: Client):
        self.clients.append(client)

    def remove_client(self, id: int):
        self.clients = list(filter(lambda c: c.id != id), self.clients)


    def get_item(self, id=None, name=None):
        try:
            if id is not None:
                return list(filter(lambda c: c.id == id, self.items))[0]
            elif name is not None:
                return list(filter(lambda c: c.name == name, self.items))[0]
            else:
                return None
        except:
            return None

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, id: int):
        self.items = list(filter(lambda c: c.id != id, self.items))
