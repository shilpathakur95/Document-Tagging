# Generated by Django 2.0.3 on 2018-04-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20180429_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='similarity',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]