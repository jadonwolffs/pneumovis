# Generated by Django 2.2.4 on 2019-08-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swabs', '0011_auto_20190827_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swab',
            name='HHdsize',
            field=models.FloatField(blank=True, null=True),
        ),
    ]