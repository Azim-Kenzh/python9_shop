from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fileds):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return  self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is False:
            raise ValueError('Super users must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, primary_key=True)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_staff


# TODO: Отображение продуктов и категорий +++++
# TODO: Регистрация, Активация, ЛОгин
# TODO: Загрузка и отображение картинок
# TODO: Верстка
# TODO: Формы
# TODO: CRUD
# TODO: поиск и фильтрация
# TODO: пагинация