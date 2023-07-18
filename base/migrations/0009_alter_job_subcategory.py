# Generated by Django 4.2.3 on 2023-07-08 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_user_is_staff_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='subCategory',
            field=models.CharField(choices=[('Hospitality', (('Barista', 'متصدی بار'), ('Catering', 'پذیرایی'), ('Chef de partie', 'سرآشپز'), ('Cleaning', 'نظافت چی'), ('Cloakroom Assistant', 'دستیار رخت کن'), ('Hosting', 'میزبانی'), ('Housekeeping', 'خانه داری'), ('Kitchen Porter', 'کارگر آشپزخانه'), ('Room Service', 'سرویس اتاق'), ('Sous-Chef', 'دستیار سرآشپز'), ('Waiter', 'پیشخدمت'))), ('Retail', (('Sales Associate', 'فروشنده'), ('Stock Assistant', 'مشاور سهام'))), ('Logistics', (('Forklift Driver', 'راننده لیفتراک'), ('Driver', 'راننده'), ('Warehouse Assistant', 'انباردار')))], max_length=30),
        ),
    ]