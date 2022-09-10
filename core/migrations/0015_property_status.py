# Generated by Django 4.1.1 on 2022-09-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_for_sale_property_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('Sale', 'For Sale'), ('Rent', 'For Rent')], default='Sale', max_length=4),
        ),
    ]