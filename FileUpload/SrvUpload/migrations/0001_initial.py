# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('fileid', models.CharField(primary_key=True, serialize=False, max_length=50)),
                ('filename', models.CharField(max_length=255)),
                ('filepath', models.CharField(max_length=255)),
                ('fileext', models.CharField(max_length=10)),
                ('filesize', models.IntegerField()),
                ('sizecomplete', models.IntegerField()),
                ('uploadtime', models.DateTimeField()),
                ('bcomplete', models.BooleanField()),
            ],
        ),
    ]
