# Generated by Django 4.1.1 on 2022-09-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]