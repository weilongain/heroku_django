# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='img', default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='topPost',
            field=models.ForeignKey(to='blog.TopPost'),
        ),
    ]
