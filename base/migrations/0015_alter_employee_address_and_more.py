# Generated by Django 4.2.3 on 2023-07-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_user_has_completed_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='creditCardNumber',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='lastName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationalCardPicture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationalCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='postalCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profilePicture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]