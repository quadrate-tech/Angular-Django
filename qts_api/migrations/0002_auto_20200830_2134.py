# Generated by Django 3.1 on 2020-08-30 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qts_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ad_types',
            new_name='ad_type',
        ),
        migrations.RenameModel(
            old_name='cities',
            new_name='city',
        ),
        migrations.RenameModel(
            old_name='districts',
            new_name='district',
        ),
        migrations.RenameModel(
            old_name='promoted_ad_details',
            new_name='promoted_ad_detail',
        ),
        migrations.RenameModel(
            old_name='users',
            new_name='user',
        ),
    ]