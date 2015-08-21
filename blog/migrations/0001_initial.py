# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('preview', models.CharField(max_length=200)),
                ('body', django_markdown.models.MarkdownField()),
                ('postime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('tagName', models.CharField(max_length=20)),
                ('creattime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(to='blog.Tag'),
        ),
    ]
