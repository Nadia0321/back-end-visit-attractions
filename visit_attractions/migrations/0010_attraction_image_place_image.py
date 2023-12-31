# Generated by Django 4.2.3 on 2023-08-05 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit_attractions', '0009_comment_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='image',
            field=models.ImageField(default='images/default_image.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default='images/default_image.jpg', upload_to='images/'),
        ),
    ]
