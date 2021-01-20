# Generated by Django 3.1 on 2021-01-20 01:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0012_auto_20210120_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='seconds',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
    ]
