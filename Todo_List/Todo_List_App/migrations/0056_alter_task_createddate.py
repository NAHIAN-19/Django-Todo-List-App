# Generated by Django 4.2 on 2023-06-20 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0055_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 20, 13, 11, 5, 918478, tzinfo=datetime.timezone.utc)),
        ),
    ]