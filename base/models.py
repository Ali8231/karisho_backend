from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, UserManager
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

    def create_superuser(self, phoneNumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( phoneNumber, password, **extra_fields)

class user(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_company = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    objects = UserManager();

    USERNAME_FIELD = 'email';

class company(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE,
                                 primary_key=True, related_name='company')
    name = models.CharField(max_length=100)
    employerFirstName = models.CharField(max_length=50)
    employerLastName = models.CharField(max_length=50)
    address = models.TextField()
    phoneNumber = models.CharField(max_length=12)
    picture = models.ImageField()
    biography = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)

class employee(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE,
                                 primary_key=True, related_name='employee')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    address = models.TextField()
    phoneNumber = models.CharField(max_length=12)
    bankAccountNumber = models.CharField(max_length=25)
    picture = models.ImageField()
    biography = models.TextField(blank=True)
    resume = models.FileField()
    rating = models.FloatField(default=0.0)
    nationalCode = models.CharField(max_length=10, null=True)
    suggestedBy = models.IntegerField(default=0) # number of employers that suggest employee for work
    

