# Generated by Django 3.1.1 on 2021-02-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0013_auto_20210225_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storecheckout',
            name='fk_customer',
        ),
        migrations.RemoveField(
            model_name='storecheckout',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='storecheckout',
            name='fk_store',
        ),
        migrations.RemoveField(
            model_name='storecheckoutitems',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='storecheckoutitems',
            name='fk_store_checkout',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='StoreCheckout',
        ),
        migrations.DeleteModel(
            name='StoreCheckOutItems',
        ),
    ]