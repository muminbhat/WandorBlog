# Generated by Django 4.2.5 on 2023-09-09 04:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_newsletter_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
