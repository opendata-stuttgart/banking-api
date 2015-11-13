# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=1000)),
                ('blz', models.CharField(max_length=20)),
                ('bic', models.CharField(max_length=20)),
                ('plz', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('short_description', models.CharField(max_length=1000)),
                ('pan', models.IntegerField(blank=True, null=True)),
                ('check_calculation_method', models.CharField(max_length=2)),
                ('dataset_number', models.CharField(max_length=10)),
                ('merkmal', models.CharField(max_length=10, choices=[('1', '1'), ('2', '2')])),
                ('change_type', models.CharField(max_length=10)),
                ('is_deletion', models.BooleanField(default=False)),
                ('following_blz', models.CharField(max_length=20, blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
