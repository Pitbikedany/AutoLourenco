# Generated by Django 5.0.5 on 2024-06-12 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_faturas_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='total',
        ),
    ]
