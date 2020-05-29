from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Activity import settings


# Custom user manager
class UsersManager(BaseUserManager):
    def create_user(self, email, real_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not real_name:
            raise ValueError("User must have a real_name")

        user = self.model(
            email=self.normalize_email(email),
            real_name=real_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, real_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            real_name=real_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


# Custom user model included real name and timezone fields
class Users(AbstractBaseUser):
    id = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField(unique=True, verbose_name='email', max_length=60)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=100)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['real_name', ]

    def __str__(self):
        return self.real_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = UsersManager()


class Activities(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
