# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_config_missing'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='date_modified',
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime.fromtimestamp(
                    0, tz=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
