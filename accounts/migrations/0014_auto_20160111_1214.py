# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20151214_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 12, 14, 14, 288000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 12, 14, 14, 281000, tzinfo=utc)),
        ),
    ]
