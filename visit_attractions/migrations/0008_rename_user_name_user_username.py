# Generated by Django 4.2.3 on 2023-08-03 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit_attractions', '0007_rename_gmail_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]