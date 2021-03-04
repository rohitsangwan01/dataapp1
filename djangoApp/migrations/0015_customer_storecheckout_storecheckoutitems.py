# Generated by Django 3.1.1 on 2021-02-24 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0014_auto_20210225_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='djangoApp.address')),
                ('customer_name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('credit', models.FloatField()),
                ('loyalty_point', models.IntegerField(blank=True, null=True)),
                ('wallet_amount', models.FloatField(blank=True, null=True)),
            ],
            bases=('djangoApp.address',),
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
                ('fk_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.product')),
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
    ]