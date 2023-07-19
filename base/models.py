from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)

        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_supporter = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    has_completed_signup = models.BooleanField(default=False)

    objects = UserManager();

    USERNAME_FIELD = 'email';

class Manager(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

class Supporter(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

class Company(models.Model):

    PROVINCE_CHOICES = [
        ("AzerbayjanSharghi", "آذربایجان شرقی"),
        ("AzerbayjanGharbi", "آذربایجان غربی"),
        ("Ardebil", "اردبیل"),
        ("Isfahan", "اصفهان"),
        ("Alborz", "البرز"),
        ("Ilam", "ایلام"),
        ("Boshehr", "بوشهر"),
        ("Tehran", "تهران"),
        ("ChaharMahal", "چهارمحال و بختیاری"),
        ("KhorasanJonobi", "خراسان جنوبی"),
        ("KhorasanShomali", "خراسان شمالی"),
        ("KhorasanRazavi", "خراسان رضوی"),
        ("Khuzestan", "کردستان"),
        ("Zanjan", "زنجان"),
        ("Semnan", "سمنان"),
        ("Sistan", "سیستان و بلوچستان"),
        ("Fars", "فارس"),
        ("Qazvin", "قزوین"),
        ("Qom", "قم"),
        ("Kordestan", "کردستان"),
        ("Kerman", "کرمان"),
        ("Kermanshah", "کرمانشاه"),
        ("Kohgiloye", "کهگیلویه و بویراحمد"),
        ("Golestan", "گلستان"),
        ("Gilan", "گیلان"),
        ("Lorestan", "لرستان"),
        ("Mazandaran", "مازندران"),
        ("Markazi", "مرکزی"),
        ("Hormozgan", "هرمزگان"),
        ("Hamedan", "همدان"),
        ("Yazd", "یزد"),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                 primary_key=True, related_name='company')
    name = models.CharField(max_length=100)
    employerFirstName = models.CharField(max_length=50)
    employerLastName = models.CharField(max_length=50)
    province = models.CharField(max_length=50, blank=True,
                                choices=PROVINCE_CHOICES)
    address = models.TextField(blank=True)
    phoneNumber = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to="uploads/", null=True, blank=True)
    biography = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    accountBalance = models.FloatField(default=0)
    adsNumber = models.IntegerField(default=0)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                 primary_key=True, related_name='employee')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField(null=True, blank=True)
    address = models.TextField()
    postalCode = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=12, blank=True)
    creditCardNumber = models.CharField(max_length=16)
    profilePicture = models.ImageField(upload_to="uploads/")
    nationalCardPicture = models.ImageField(upload_to="uploads/")
    biography = models.TextField(blank=True)
    resume = models.FileField(upload_to="uploads/")
    rating = models.FloatField(default=0.0)
    ratedBy = models.IntegerField(default=0) # number of employers that rated employee
    nationalCode = models.CharField(max_length=10)
    suggestedBy = models.IntegerField(default=0) # number of employers that suggest employee for work
    skillSet = models.TextField(blank=True)
    experiences = models.TextField(blank=True)
    favorites = models.TextField(blank=True)

class Job(models.Model):

    HOSPITALITY = "Hospitality"
    RETAIL = "Retail"
    LOGISTICS = "Logistics"
    CATEGORY_CHOICES = [
        (HOSPITALITY, "مهمان داری"),
        (RETAIL, "خرده فروشی"),
        (LOGISTICS, "تدارکات"),
    ]

    SUBCATEGORY_CHOICES = [
        (
            HOSPITALITY,
            (
                ("Barista", "متصدی بار"),
                ("Catering", "پذیرایی"),
                ("Chef de partie", "سرآشپز"),
                ("Cleaning", "نظافت چی"),
                ("Cloakroom Assistant", "دستیار رخت کن"),
                ("Hosting", "میزبانی"),
                ("Housekeeping", "خانه داری"),
                ("Kitchen Porter", "کارگر آشپزخانه"),
                ("Room Service", "سرویس اتاق"),
                ("Sous-Chef", "دستیار سرآشپز"),
                ("Waiter", "پیشخدمت"),
            ),
        ),
        (
            RETAIL,
            (
                ("Sales Associate", "فروشنده"),
                ("Stock Assistant", "مشاور سهام"),
            ),
        ),
        (
            LOGISTICS,
            (
                ("Forklift Driver", "راننده لیفتراک"),
                ("Driver", "راننده"),
                ("Warehouse Assistant", "انباردار"),
            ),
        ),
    ]


    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=50)
    jobDescription = models.TextField()
    requiredSkills = models.TextField()
    rules = models.TextField()
    category = models.CharField(max_length=25,
                                choices=CATEGORY_CHOICES)
    subCategory = models.CharField(max_length=30,
                                   choices=SUBCATEGORY_CHOICES)
    minimumHourlySalary = models.FloatField()
    address = models.TextField()

class Shift(models.Model):
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    salary = models.FloatField()
    numberOfApplicants = models.IntegerField()

    class Meta:
        unique_together = ('job', 'date', 'startTime', 'endTime')

class JobApplication(models.Model):

    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    PENDING = "Pending"
    STATUS_CHOICES = [
        (ACCEPTED, "قبول شده"),
        (REJECTED, "رد شده"),
        (PENDING, "در حال بررسی"),
    ]

    shift = models.ForeignKey(to=Shift, on_delete=models.CASCADE)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('shift', 'employee')
