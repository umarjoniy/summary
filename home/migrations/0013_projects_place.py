# Generated by Django 4.0.6 on 2022-07-30 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_services_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='place',
            field=models.IntegerField(default=0),
        ),
    ]
