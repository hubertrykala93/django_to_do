from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.utils.timezone import now
from .validators import username_validate, email_validate
from PIL import Image


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('You have not provided a valid e-mail address.')

        email = self.normalize_email(email=email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username=username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username=username, email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False, default='',
                                validators=[username_validate])
    email = models.EmailField(blank=True, default='', unique=True, validators=[email_validate])
    first_name = models.CharField(max_length=50, unique=False, null=False, blank=False, default='User')
    last_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(default='Not Defined', max_length=20, choices=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    ))
    image = models.ImageField(
        default='', upload_to='profile_pics')
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.gender == 'Male':
            self.image = 'default_male_pic.jpg'
        elif self.gender == 'Female':
            self.image = 'default_female_pic.jpg'

        super(User, self).save(*args, **kwargs)

        img = Image.open(fp=self.image.path)

        if img.mode == 'RGBA':
            img = img.convert(mode='RGB')

        if img.width > 300 or img.height > 300:
            img.thumbnail(size=(300, 300))
            img.save(fp=self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile.'