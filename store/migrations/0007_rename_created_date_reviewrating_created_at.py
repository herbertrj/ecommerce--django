# Generated by Django 5.0.2 on 2024-02-19 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_created_at_reviewrating_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrating',
            old_name='created_date',
            new_name='created_at',
        ),
    ]
