# Generated by Django 3.1.1 on 2021-02-21 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0009_storecheckout_fk_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='fk_address',
        ),
    ]
