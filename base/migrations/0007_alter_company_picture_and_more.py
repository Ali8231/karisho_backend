# Generated by Django 4.2.3 on 2023-07-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_shift_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationalCardPicture',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profilePicture',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
