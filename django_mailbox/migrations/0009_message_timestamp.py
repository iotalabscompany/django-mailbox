# Generated by Django 3.1.4 on 2022-10-17 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0008_auto_20190219_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Timestamp'),
            preserve_default=False,
        ),
    ]
