# Generated by Django 4.2 on 2023-06-15 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0046_profile_completed_tasks_count_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 10, 59, 30, 190355, tzinfo=datetime.timezone.utc)),
        ),
    ]