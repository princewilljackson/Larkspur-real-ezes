# Generated by Django 4.1.1 on 2022-09-10 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_aboutcontact_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='reserved',
            new_name='for_sale',
        ),
    ]
