# Generated by Django 3.2 on 2021-05-13 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverecord',
            name='leave_type',
            field=models.CharField(choices=[('1', 'ANNUAL LEAVE'), ('2', 'EMERGENCY LEAVE'), ('3', 'MEDICAL LEAVE'), ('4', 'OTHERS')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employeeleave_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeepersonalinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employeepersonalinfo_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employmentinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employmentinfo_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leaverecord',
            name='leave_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaverecord',
            name='leave_status',
            field=models.CharField(choices=[('1', 'APPROVED'), ('2', 'CANCELED'), ('3', 'PENDING')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='leaverecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leavereocrd_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
