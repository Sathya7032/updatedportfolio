# Generated by Django 5.2 on 2025-04-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_c',
        ),
        migrations.DeleteModel(
            name='Dairy',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=1),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
