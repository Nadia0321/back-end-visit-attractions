# Generated by Django 4.2.3 on 2023-08-03 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit_attractions', '0006_remove_user_password_user_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gmail',
            new_name='email',
        ),
    ]