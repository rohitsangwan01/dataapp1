# Generated by Django 3.1.1 on 2021-02-20 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangoApp', '0002_auto_20210220_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=1)),
                ('image_link', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=1)),
                ('image_link', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('credit', models.FloatField()),
                ('loyalty_point', models.IntegerField(blank=True, null=True)),
                ('wallet_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Microenterpreneur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=1)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('article_code', models.CharField(blank=True, max_length=100, null=True)),
                ('pack_qty', models.IntegerField(blank=True, null=True)),
                ('metric_unit', models.CharField(blank=True, max_length=100, null=True)),
                ('uom', models.CharField(blank=True, max_length=100, null=True)),
                ('pack_site', models.IntegerField(blank=True, null=True)),
                ('pack_type', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('is_online', models.BooleanField(blank=True, null=True)),
                ('is_expirable', models.BooleanField(blank=True, null=True)),
                ('fk_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.brand')),
                ('fk_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBarCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=1)),
                ('fk_product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_number', models.TextField(max_length=50)),
                ('sales_invoice_number', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('store_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreCheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('invoice_number', models.CharField(max_length=100)),
                ('is_delivery', models.BooleanField()),
                ('is_online', models.BooleanField()),
                ('promotions', models.CharField(blank=True, max_length=100, null=True)),
                ('cast_discount', models.FloatField()),
                ('sub_total', models.FloatField()),
                ('grand_total', models.FloatField()),
                ('payments', models.FloatField(blank=True, null=True)),
                ('loyalty_point_used', models.IntegerField(blank=True, null=True)),
                ('wallet_amount_used', models.FloatField(blank=True, null=True)),
                ('fk_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.customer')),
                ('fk_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.store')),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('pincode', models.IntegerField()),
                ('geolocation', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.state')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=1)),
                ('warehouse_code', models.IntegerField()),
                ('fk_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.warehouseaddress')),
            ],
        ),
        migrations.CreateModel(
            name='StoreInventoryTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mrp', models.FloatField()),
                ('expiry_date', models.DateField()),
                ('batch_number', models.IntegerField()),
                ('txn_type', models.CharField(choices=[('stock_transfer', 'stock_transfer'), ('stock_return', 'stock_return'), ('local_purchase', 'local_purchase'), ('stock_audit_adjustment', 'stock_audit_adjustment'), ('pos_returns', 'pos_returns')], max_length=100)),
                ('reference_number', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('fk_barcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.productbarcode')),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
                ('fk_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.store')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='StoreInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrp', models.FloatField(default=False)),
                ('quantity', models.IntegerField(default=False)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('fk_product', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
                ('fk_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreCheckOutItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('mrp', models.FloatField()),
                ('sp', models.CharField(max_length=100)),
                ('attributed_cart_discount', models.FloatField()),
                ('fk_product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
                ('fk_store_checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.storecheckout')),
            ],
        ),
        migrations.CreateModel(
            name='StoreAssortment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1)),
                ('min_qty', models.IntegerField(blank=True, null=True)),
                ('max_qty', models.IntegerField(blank=True, null=True)),
                ('sp', models.IntegerField(blank=True, null=True)),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
                ('fk_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('pincode', models.IntegerField()),
                ('geolocation', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.state')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.storeaddress'),
        ),
        migrations.AddField(
            model_name='store',
            name='fk_microenterpreneur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.microenterpreneur'),
        ),
        migrations.CreateModel(
            name='StocktransferItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrp', models.FloatField()),
                ('expiry_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('fk_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
                ('fk_stock_transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.stocktransfer')),
            ],
        ),
        migrations.AddField(
            model_name='stocktransfer',
            name='fk_store',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.store'),
        ),
        migrations.CreateModel(
            name='MicroenterpreneurAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('pincode', models.IntegerField()),
                ('geolocation', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.state')),
            ],
        ),
        migrations.AddField(
            model_name='microenterpreneur',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.microenterpreneuraddress'),
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('pincode', models.IntegerField()),
                ('geolocation', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.state')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='fk_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.customeraddress'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.state'),
        ),
        migrations.AddField(
            model_name='category',
            name='fk_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.manufacturer'),
        ),
        migrations.AddField(
            model_name='brand',
            name='fk_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoApp.manufacturer'),
        ),
    ]
