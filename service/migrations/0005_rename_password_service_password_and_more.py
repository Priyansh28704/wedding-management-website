# Generated by Django 5.1.1 on 2024-12-22 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_rename_phone_service_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='email',
            new_name='submit',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='Name',
            new_name='username',
        ),
    ]
