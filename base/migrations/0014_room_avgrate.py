# Generated by Django 4.1.4 on 2023-01-25 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_room_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='avgrate',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
