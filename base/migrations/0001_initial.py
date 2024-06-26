# Generated by Django 4.2.3 on 2023-07-25 14:35

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_company', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_supporter', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('has_completed_signup', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', base.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=50)),
                ('jobDescription', models.TextField()),
                ('picture', models.ImageField(null=True, upload_to='uploads/')),
                ('requiredSkills', models.TextField()),
                ('rules', models.TextField()),
                ('category', models.CharField(choices=[('Hospitality', 'مهمان داری'), ('Retail', 'خرده فروشی'), ('Logistics', 'تدارکات')], max_length=25)),
                ('subCategory', models.CharField(choices=[('Hospitality', (('Barista', 'متصدی بار'), ('Catering', 'پذیرایی'), ('Chef de partie', 'سرآشپز'), ('Cleaning', 'نظافت چی'), ('Cloakroom Assistant', 'دستیار رخت کن'), ('Hosting', 'میزبانی'), ('Housekeeping', 'خانه داری'), ('Kitchen Porter', 'کارگر آشپزخانه'), ('Room Service', 'سرویس اتاق'), ('Sous-Chef', 'دستیار سرآشپز'), ('Waiter', 'پیشخدمت'))), ('Retail', (('Sales Associate', 'فروشنده'), ('Stock Assistant', 'مشاور سهام'))), ('Logistics', (('Forklift Driver', 'راننده لیفتراک'), ('Driver', 'راننده'), ('Warehouse Assistant', 'انباردار')))], max_length=30)),
                ('minimumHourlySalary', models.FloatField(null=True)),
                ('address', models.TextField()),
                ('has_shift', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('employerFirstName', models.CharField(max_length=50)),
                ('employerLastName', models.CharField(max_length=50)),
                ('province', models.CharField(blank=True, choices=[('AzerbayjanSharghi', 'آذربایجان شرقی'), ('AzerbayjanGharbi', 'آذربایجان غربی'), ('Ardebil', 'اردبیل'), ('Isfahan', 'اصفهان'), ('Alborz', 'البرز'), ('Ilam', 'ایلام'), ('Boshehr', 'بوشهر'), ('Tehran', 'تهران'), ('ChaharMahal', 'چهارمحال و بختیاری'), ('KhorasanJonobi', 'خراسان جنوبی'), ('KhorasanShomali', 'خراسان شمالی'), ('KhorasanRazavi', 'خراسان رضوی'), ('Khuzestan', 'کردستان'), ('Zanjan', 'زنجان'), ('Semnan', 'سمنان'), ('Sistan', 'سیستان و بلوچستان'), ('Fars', 'فارس'), ('Qazvin', 'قزوین'), ('Qom', 'قم'), ('Kordestan', 'کردستان'), ('Kerman', 'کرمان'), ('Kermanshah', 'کرمانشاه'), ('Kohgiloye', 'کهگیلویه و بویراحمد'), ('Golestan', 'گلستان'), ('Gilan', 'گیلان'), ('Lorestan', 'لرستان'), ('Mazandaran', 'مازندران'), ('Markazi', 'مرکزی'), ('Hormozgan', 'هرمزگان'), ('Hamedan', 'همدان'), ('Yazd', 'یزد')], max_length=50)),
                ('address', models.TextField(blank=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=12)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('biography', models.TextField(blank=True)),
                ('rating', models.FloatField(default=0.0)),
                ('accountBalance', models.FloatField(default=0)),
                ('adsNumber', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employee', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birthDate', models.DateField(blank=True, null=True)),
                ('address', models.TextField()),
                ('postalCode', models.CharField(max_length=10)),
                ('phoneNumber', models.CharField(blank=True, max_length=12)),
                ('creditCardNumber', models.CharField(max_length=16)),
                ('profilePicture', models.ImageField(upload_to='uploads/')),
                ('nationalCardPicture', models.ImageField(upload_to='uploads/')),
                ('biography', models.TextField(blank=True)),
                ('resume', models.FileField(upload_to='uploads/')),
                ('rating', models.FloatField(default=0.0)),
                ('ratedBy', models.IntegerField(default=0)),
                ('nationalCode', models.CharField(max_length=10)),
                ('suggestedBy', models.IntegerField(default=0)),
                ('skillSet', models.TextField(blank=True)),
                ('experiences', models.TextField(blank=True)),
                ('favorites', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('salary', models.FloatField()),
                ('numberOfApplicants', models.IntegerField(default=0)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.job')),
            ],
            options={
                'unique_together': {('job', 'date', 'startTime', 'endTime')},
            },
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.company'),
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Accepted', 'قبول شده'), ('Rejected', 'رد شده'), ('Pending', 'در حال بررسی')], max_length=20)),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.shift')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.employee')),
            ],
            options={
                'unique_together': {('shift', 'employee')},
            },
        ),
    ]
