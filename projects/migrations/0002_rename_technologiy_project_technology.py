# Generated by Django 4.2.1 on 2023-05-30 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='technologiy',
            new_name='technology',
        ),
    ]
