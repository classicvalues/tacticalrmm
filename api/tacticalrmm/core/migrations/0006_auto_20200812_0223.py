# Generated by Django 3.1 on 2020-08-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200712_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coresettings',
            name='smtp_host_user',
            field=models.CharField(blank=True, default='admin@example.com', max_length=255, null=True),
        ),
    ]
