# Generated by Django 2.2.13 on 2021-02-27 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_v0_4_7'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='lang',
            field=models.CharField(default='en', help_text='Two-letter ISO 639 code for the preferred communication language (ex: en)', max_length=5, verbose_name='Preferred communication language'),
        )
    ]
