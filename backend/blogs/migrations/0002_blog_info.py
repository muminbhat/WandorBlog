# Generated by Django 4.2.5 on 2023-09-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='info',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
