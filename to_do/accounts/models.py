from django.db import models
from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.utils.timezone import now
from PIL import Image
from django.core.validators import ValidationError


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
                                db_column='user_username')
    email = models.EmailField(blank=True, default='', unique=True, validators=[ValidationError], db_column='user_email')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, db_column='user_image')

    is_verified = models.BooleanField(default=False, db_column='user_is_verified')
    is_active = models.BooleanField(default=True, db_column='user_is_active')
    is_superuser = models.BooleanField(default=False, db_column='user_is_superuser')
    is_staff = models.BooleanField(default=False, db_column='user_is_staff')
    date_joined = models.DateTimeField(default=now, db_column='user_date_joined')
    last_login = models.DateTimeField(blank=True, null=True, db_column='user_last_login')

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
        super(User, self).save(*args, **kwargs)

        img = Image.open(fp=self.image.path)

        if img.mode == 'RGBA':
            img = img.convert(mode='RGB')

        if img.width > 300 or img.height > 300:
            img.thumbnail(size=(300, 300))
            img.save(fp=self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, db_column='user_profile')
    first_name = models.CharField(max_length=50, unique=False, null=True, blank=True, db_column='profile_first_name')
    last_name = models.CharField(max_length=50, blank=True, null=True, db_column='profile_last_name')
    gender = models.CharField(default='', max_length=20, choices=(
        ('Not Defined', 'Not Defined'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ), db_column='profile_gender')
    date_of_birth = models.CharField(max_length=20, blank=True, null=True, db_column='profile_date_of_birth')
    country = models.CharField(max_length=50, blank=True, null=True, db_column='profile_country')
    province = models.CharField(max_length=50, blank=True, null=True, db_column='profile_province')
    city = models.CharField(max_length=50, blank=True, null=True, db_column='profile_city')

    def __str__(self):
        return f'{self.user.username} Profile.'
