from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    """Модель Привычки"""

    user = models.ForeignKey(
        AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE
    )

    place = models.CharField(max_length=100, verbose_name="Место")

    time = models.TimeField(verbose_name="Время начала выполнения привычки")

    action = models.CharField(max_length=100, verbose_name="Действие")

    pleasant_habit = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )

    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )

    frequency_habit = models.IntegerField(default=1, verbose_name='Периодичность привычки в днях')

    award = models.CharField(max_length=100, verbose_name="Вознаграждение", **NULLABLE)

    time_complete = models.DurationField(default=timedelta(seconds=120), verbose_name="Время на выполнение")

    is_public = models.BooleanField(default=True, verbose_name="Публичная привычка")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.user}: Я буду {self.action} сегодня в {self.time} {self.place}!"
