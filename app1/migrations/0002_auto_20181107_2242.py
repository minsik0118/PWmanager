# Generated by Django 2.1.2 on 2018-11-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_number',
            field=models.IntegerField(default=0),
        ),
    ]
