# Generated by Django 3.2 on 2021-05-19 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0007_alter_countryfiles_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualCountryLinkDirectory',
            fields=[
                ('countylinkdirectory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='country.countylinkdirectory')),
                ('year_1', models.DateField()),
                ('year_2', models.DateField()),
                ('year_3', models.DateField()),
                ('year_4', models.DateField()),
                ('year_5', models.DateField()),
                ('year_6', models.DateField()),
                ('year_7', models.DateField()),
                ('year_8', models.DateField()),
                ('year_9', models.DateField()),
            ],
            options={
                'verbose_name': 'Annual Country LinkDirectory',
                'verbose_name_plural': 'Annual Country LinkDirectory',
            },
            bases=('country.countylinkdirectory',),
        ),
        migrations.CreateModel(
            name='MonthCountryLinkDirectory',
            fields=[
                ('countylinkdirectory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='country.countylinkdirectory')),
                ('month_1', models.DateField()),
                ('month_2', models.DateField()),
                ('month_3', models.DateField()),
                ('month_4', models.DateField()),
                ('month_5', models.DateField()),
                ('month_6', models.DateField()),
                ('month_7', models.DateField()),
                ('month_8', models.DateField()),
                ('month_9', models.DateField()),
                ('month_10', models.DateField()),
                ('month_11', models.DateField()),
                ('month_12', models.DateField()),
                ('month_13', models.DateField()),
                ('month_14', models.DateField()),
                ('month_15', models.DateField()),
                ('month_16', models.DateField()),
                ('month_17', models.DateField()),
                ('month_18', models.DateField()),
                ('month_19', models.DateField()),
                ('month_20', models.DateField()),
                ('month_21', models.DateField()),
                ('month_22', models.DateField()),
                ('month_23', models.DateField()),
                ('month_24', models.DateField()),
            ],
            options={
                'verbose_name': 'Month Country LinkDirectory',
                'verbose_name_plural': 'Month Country LinkDirectory',
            },
            bases=('country.countylinkdirectory',),
        ),
        migrations.CreateModel(
            name='QuarterCountryLinkDirectory',
            fields=[
                ('countylinkdirectory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='country.countylinkdirectory')),
                ('quarter_1', models.DateField()),
                ('quarter_2', models.DateField()),
                ('quarter_3', models.DateField()),
                ('quarter_4', models.DateField()),
                ('quarter_5', models.DateField()),
                ('quarter_6', models.DateField()),
                ('quarter_7', models.DateField()),
                ('quarter_8', models.DateField()),
                ('quarter_9', models.DateField()),
                ('quarter_10', models.DateField()),
                ('quarter_11', models.DateField()),
                ('quarter_12', models.DateField()),
                ('quarter_13', models.DateField()),
                ('quarter_14', models.DateField()),
            ],
            options={
                'verbose_name': 'Quarter Country LinkDirectory',
                'verbose_name_plural': 'Quarter Country LinkDirectory',
            },
            bases=('country.countylinkdirectory',),
        ),
        migrations.RemoveField(
            model_name='countylinkdirectory',
            name='frequency',
        ),
    ]