# Generated by Django 2.1.2 on 2018-12-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20181204_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='urls',
            field=models.CharField(max_length=200),
        ),
    ]
