# Generated by Django 4.2 on 2023-11-05 12:38

import Todo_List_App.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0003_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.jpg', upload_to=Todo_List_App.models.profile_picture_path),
        ),
    ]