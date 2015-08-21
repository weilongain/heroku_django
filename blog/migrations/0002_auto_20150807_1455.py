# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('topName', models.CharField(max_length=20)),
                ('creattime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='topPost',
            field=models.ForeignKey(default=None, to='blog.TopPost'),
        ),
    ]
