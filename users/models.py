from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None  # убираем username
    email = models.EmailField(unique=True, verbose_name="Email")

    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Страна")

    USERNAME_FIELD = 'email'  # авторизация по email
    REQUIRED_FIELDS = []  # не требуем username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
