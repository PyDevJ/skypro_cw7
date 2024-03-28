from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Model for users"""
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    chat_id = models.TextField(verbose_name='id чата в телеграмм', **NULLABLE)
    telegram_user_name = models.CharField(max_length=200, verbose_name='имя в телеграмм', unique=True, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
