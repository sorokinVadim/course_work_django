# Generated by Django 4.0.4 on 2022-05-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawnshop', '0002_alter_client_age_alter_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport_num',
            field=models.IntegerField(max_length=1000000000, unique=True, verbose_name='Номер паспорта'),
        ),
    ]
