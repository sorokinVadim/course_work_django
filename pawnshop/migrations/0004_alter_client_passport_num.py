# Generated by Django 4.0.4 on 2022-06-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0003_alter_client_passport_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport_num',
            field=models.IntegerField(unique=True, verbose_name='Номер паспорта'),
        ),
    ]
