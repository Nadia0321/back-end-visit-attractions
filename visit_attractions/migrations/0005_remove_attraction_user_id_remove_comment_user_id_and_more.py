# Generated by Django 4.2.3 on 2023-07-31 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit_attractions', '0004_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='place',
            name='user_id',
        ),
    ]
