# Generated by Django 4.2.3 on 2023-08-16 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit_attractions', '0016_rename_image_attraction_imagea_attraction_imageb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attraction',
            old_name='imageA',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='attraction',
            name='imageB',
        ),
    ]
