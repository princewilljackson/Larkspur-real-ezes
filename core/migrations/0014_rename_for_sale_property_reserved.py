# Generated by Django 4.1.1 on 2022-09-10 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_reserved_property_for_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='for_sale',
            new_name='reserved',
        ),
    ]
