# Generated by Django 3.1 on 2020-08-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200811_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerelease',
            name='pre_release',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]