# Generated by Django 5.1.1 on 2024-12-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_password_service_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='submit',
        ),
    ]
