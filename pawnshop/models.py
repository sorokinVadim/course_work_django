from django.db.models import *
from django.urls import reverse


class Client(Model):
    first_name = CharField(max_length=30, verbose_name="И'мя")
    last_name = CharField(max_length=30, verbose_name="Прізвище")
    age = IntegerField(verbose_name="Вік")
    passport_num = CharField(max_length=8, verbose_name="Номер паспорта")

    def get_absolute_url(self):
        return reverse('client', args=[str(self.id)])

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

    def __str__(self):
        return f'{self.name}'

