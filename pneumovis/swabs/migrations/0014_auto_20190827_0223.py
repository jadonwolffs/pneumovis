# Generated by Django 2.2.4 on 2019-08-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swabs', '0013_auto_20190827_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swab',
            name='geo_lat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='swab',
            name='geo_long',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
