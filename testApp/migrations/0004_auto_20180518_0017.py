# Generated by Django 2.0.3 on 2018-05-17 18:47

from django.db import migrations, models
import testApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_input_similarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='data',
            field=models.FileField(storage=testApp.models.OverwriteStorage(), upload_to=''),
        ),
    ]
