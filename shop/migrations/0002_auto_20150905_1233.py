# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyer',
            options={'verbose_name': 'Buyer'},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Seller'},
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='login_email',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='unit',
            field=models.ForeignKey(to='shop.Unit'),
        ),
    ]
