# Generated by Django 4.2.3 on 2023-08-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit_attractions', '0014_alter_attraction_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='created_by',
            field=models.CharField(default='Nadia123'),
        ),
    ]
