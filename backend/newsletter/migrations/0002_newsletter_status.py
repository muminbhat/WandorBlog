# Generated by Django 4.2.5 on 2023-09-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
