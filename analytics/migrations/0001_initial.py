# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
                ('post_id', models.CharField(unique=True, max_length=64)),
                ('text', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
