# Generated by Django 3.1.1 on 2021-02-24 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0012_auto_20210224_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='fk_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoApp.address'),
        ),
    ]
