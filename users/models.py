from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель Пользователя"""
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите электронную почту",
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        **NULLABLE
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        help_text="Добавьте аватар",
        **NULLABLE
    )

    telegram_id = models.CharField(
        max_length=50,
        verbose_name="Телеграмм ID",
        help_text="Укажите телеграмм ID",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
