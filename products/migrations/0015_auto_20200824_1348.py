# Generated by Django 3.1 on 2020-08-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200822_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pre_release',
            new_name='release_date',
        ),
        migrations.AddField(
            model_name='product',
            name='is_pre_release',
            field=models.BooleanField(default=False),
        ),
    ]