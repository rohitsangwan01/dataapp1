# Generated by Django 3.1.1 on 2021-02-26 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0015_customer_storecheckout_storecheckoutitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocktransfer',
            name='fk_store',
        ),
        migrations.RemoveField(
            model_name='stocktransferitems',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='stocktransferitems',
            name='fk_stock_transfer',
        ),
        migrations.RemoveField(
            model_name='store',
            name='fk_address',
        ),
        migrations.RemoveField(
            model_name='store',
            name='fk_microenterpreneur',
        ),
        migrations.RemoveField(
            model_name='storeassortment',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='storeassortment',
            name='fk_store',
        ),
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
        migrations.RemoveField(
            model_name='storeinventory',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='storeinventory',
            name='fk_store',
        ),
        migrations.RemoveField(
            model_name='storeinventorytransactions',
            name='fk_barcode',
        ),
        migrations.RemoveField(
            model_name='storeinventorytransactions',
            name='fk_product',
        ),
        migrations.RemoveField(
            model_name='storeinventorytransactions',
            name='fk_store',
        ),
        migrations.DeleteModel(
            name='Microenterpreneur',
        ),
        migrations.DeleteModel(
            name='StockTransfer',
        ),
        migrations.DeleteModel(
            name='StocktransferItems',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.DeleteModel(
            name='StoreAssortment',
        ),
        migrations.DeleteModel(
            name='StoreCheckout',
        ),
        migrations.DeleteModel(
            name='StoreCheckOutItems',
        ),
        migrations.DeleteModel(
            name='StoreInventory',
        ),
        migrations.DeleteModel(
            name='StoreInventoryTransactions',
        ),
    ]
