# Generated by Django 4.1.3 on 2023-03-20 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_alter_task_tile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Tile',
        ),
    ]