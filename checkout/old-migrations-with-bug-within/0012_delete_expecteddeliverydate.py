# Generated by Django 3.1 on 2020-08-25 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_auto_20200825_0806'),
    ]

    operations = [
        migrations.DeleteModel(
            name='expectedDeliveryDate',
        ),
    ]