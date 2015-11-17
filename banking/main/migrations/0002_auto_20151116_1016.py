# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='plz',
            new_name='zipcode',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='description',
        ),
    ]
