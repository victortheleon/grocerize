# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150905_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='login_email',
            field=models.CharField(max_length=200),
        ),
    ]
