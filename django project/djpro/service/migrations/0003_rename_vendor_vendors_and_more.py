# Generated by Django 5.1.1 on 2024-12-20 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_vendor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vendor',
            new_name='Vendors',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_icon',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_city',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_type',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='vendors',
            old_name='vendor_type',
            new_name='vendors_type',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_des',
        ),
    ]