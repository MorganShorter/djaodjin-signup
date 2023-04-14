# Generated by Django 2.2.13 on 2021-02-01 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_0_2_8'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='verification_key',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_verification_at',
            field=models.DateTimeField(help_text='Date/time when the e-mail verification key was sent', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_verification_key',
            field=models.CharField(max_length=40, null=True, verbose_name='Email verification key'),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_verified_at',
            field=models.DateTimeField(help_text='Date/time when the e-mail was last verified', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number to contact user', max_length=128, null=True, region=None, unique=True, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_verification_at',
            field=models.DateTimeField(help_text='Date/time when the phone verification key was sent', null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_verification_key',
            field=models.CharField(max_length=40, null=True, verbose_name='Phone verification key'),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_verified_at',
            field=models.DateTimeField(help_text='Date/time when the phone number was last verified', null=True),
        ),
        migrations.AddField(
            model_name='credentials',
            name='extra',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='account',
            field=models.ForeignKey(help_text='Account the activity is associated to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date/time of creation (in ISO format)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='created_by',
            field=models.ForeignKey(help_text='User that created the activity', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='text',
            field=models.TextField(blank=True, help_text='Free form text description of the activity'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date/time of creation (in ISO format)'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='extra',
            field=models.TextField(help_text='Extra meta data (can be stringify JSON)', null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(blank=True, help_text='Full name (effectively first name followed by last name)', max_length=60, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.URLField(blank=True, help_text='URL location of the profile picture', max_length=2083, null=True, verbose_name='URL to a profile picture'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(help_text='Unique identifier shown in the URL bar, effectively the username for profiles with login credentials.', unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='slug',
            field=models.SlugField(choices=[], help_text='Unique identifier shown in the URL bar', unique=True),
        ),
    ]
