# Generated by Django 3.0.3 on 2020-02-23 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('initial_page', '0002_auto_20200223_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='your_pref',
            new_name='prefecture',
        ),
    ]
