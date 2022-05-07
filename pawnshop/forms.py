from django.forms import ModelForm, DateInput, ValidationError
from .models import *
from datetime import date

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


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
