from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Расширенная модель пользователя"""

    READING_LEVELS = [
        ('BEGINNER', 'Начинающий'),
        ('INTERMEDIATE', 'Средний'),
        ('ADVANCED', 'Продвинутый'),
    ]

    bio = models.TextField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    reading_level = models.CharField(
        max_length=20,
        choices=READING_LEVELS,
        default='INTERMEDIATE',
        blank=True
                                     )

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} ({self.username})"
        else:
            return self.username
        
