# Generated by Django 3.0.6 on 2020-05-31 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
