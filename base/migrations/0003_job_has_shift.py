# Generated by Django 4.2.3 on 2023-07-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_job_picture_alter_job_minimumhourlysalary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='has_shift',
            field=models.BooleanField(default=False),
        ),
    ]
