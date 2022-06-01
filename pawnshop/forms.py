from django.forms import ModelForm, DateInput, ValidationError, Form
from django import forms
from .models import *
from datetime import date


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean_passport_num(self):
        if self.cleaned_data["passport_num"] > 1000000000:
            raise ValidationError("Номер паспорту не може мати більше 8 цифр")
        return self.cleaned_data["passport_num"]


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'save_until': DateInput(attrs={'type': 'date'})
        }

    def clean_save_until(self):
        if self.cleaned_data['save_until'] < date.today():
            raise ValidationError("Дата повинна бути не більше не раніше ніж сьогодні")
        return self.cleaned_data['save_until']


class SearchForm(Form):
    item_name = forms.CharField(label="Найменування товару", required=False)
    passport_num = forms.IntegerField(label="Номер паспорта", required=False)
    client_id = forms.IntegerField(label="ID клієнта", required=False)
    item_id = forms.IntegerField(label="ID предмета", required=False)

