# Generated by Django 2.0.7 on 2018-11-05 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20181105_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movers',
            name='services',
        ),
    ]
