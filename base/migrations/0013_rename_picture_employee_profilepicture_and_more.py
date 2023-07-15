# Generated by Django 4.2.3 on 2023-07-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_company_province'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='picture',
            new_name='profilePicture',
        ),
        migrations.AddField(
            model_name='company',
            name='accountBalance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='adsNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='employee',
            name='experiences',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='favorites',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='nationalCardPicture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='postalCode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='skillSet',
            field=models.TextField(blank=True),
        ),
    ]
