# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151116_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bic',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
    ]
