# Generated by Django 3.1.1 on 2021-02-20 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='fk_manufacturer',
        ),
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fk_address',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='microenterpreneur',
            name='fk_address',
        ),
        migrations.RemoveField(
            model_name='microenterpreneuraddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='microenterpreneuraddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fk_brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fk_category',
        ),
        migrations.RemoveField(
            model_name='productbarcode',
            name='fk_product',
        ),
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
            model_name='storeaddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='storeaddress',
            name='state',
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
        migrations.RemoveField(
            model_name='warehouse',
            name='fk_address',
        ),
        migrations.RemoveField(
            model_name='warehouseaddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='warehouseaddress',
            name='state',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='CustomerAddress',
        ),
        migrations.DeleteModel(
            name='Manufacturer',
        ),
        migrations.DeleteModel(
            name='Microenterpreneur',
        ),
        migrations.DeleteModel(
            name='MicroenterpreneurAddress',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductBarCode',
        ),
        migrations.DeleteModel(
            name='State',
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
            name='StoreAddress',
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
        migrations.DeleteModel(
            name='Warehouse',
        ),
        migrations.DeleteModel(
            name='WarehouseAddress',
        ),
    ]
