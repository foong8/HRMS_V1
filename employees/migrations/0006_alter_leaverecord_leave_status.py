# Generated by Django 3.2 on 2021-05-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_leaverecord_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverecord',
            name='leave_status',
            field=models.CharField(choices=[('1', 'APPROVED'), ('2', 'CANCELED'), ('3', 'PENDING')], default='3', max_length=1),
        ),
    ]
