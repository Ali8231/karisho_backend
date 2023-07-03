# Generated by Django 4.2.3 on 2023-07-03 14:48

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_company', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', base.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('employerFirstName', models.CharField(max_length=50)),
                ('employerLastName', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=12)),
                ('picture', models.ImageField(upload_to='')),
                ('biography', models.TextField()),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employee', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birthDate', models.DateField()),
                ('address', models.TextField()),
                ('phoneNumber', models.CharField(max_length=12)),
                ('bankAccountNumber', models.CharField(max_length=25)),
                ('picture', models.ImageField(upload_to='')),
                ('biography', models.TextField()),
                ('resume', models.FileField(upload_to='')),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
    ]
