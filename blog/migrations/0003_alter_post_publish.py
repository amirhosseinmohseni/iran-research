# Generated by Django 4.1.7 on 2023-05-07 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 5, 7, 13, 30, 45, 215494, tzinfo=datetime.timezone.utc)),
        ),
    ]