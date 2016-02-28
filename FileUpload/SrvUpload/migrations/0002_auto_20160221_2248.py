# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SrvUpload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinfo',
            name='bcomplete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='sizecomplete',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='uploadtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
