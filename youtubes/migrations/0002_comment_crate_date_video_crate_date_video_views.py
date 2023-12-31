# Generated by Django 4.2.3 on 2023-07-30 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='crate_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 30, 12, 49, 56, 107254, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='video',
            name='crate_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 30, 12, 49, 56, 106277, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
