# Generated by Django 3.2 on 2021-05-18 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_auto_20210518_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryassignment',
            name='country_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='country.countrybaseinfo'),
        ),
    ]
