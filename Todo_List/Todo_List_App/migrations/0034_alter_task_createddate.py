# Generated by Django 4.2 on 2023-06-13 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0033_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 13, 10, 36, 28, 799295, tzinfo=datetime.timezone.utc)),
        ),
    ]