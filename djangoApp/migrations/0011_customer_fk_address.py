# Generated by Django 3.1.1 on 2021-02-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0010_remove_customer_fk_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='fk_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.address'),
        ),
    ]