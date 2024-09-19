from datetime import timedelta

from rest_framework.exceptions import ValidationError


class ChoiceRewardValidator:
    """Исключает одновременный выбор награды и приятной привычки."""

    def __init__(self, related_habit, award):
        self.related_habit = related_habit
        self.award = award

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.award):
            raise ValidationError(f"""Нельзя выбрать приятную привычку и награду одновременно.""")


class TimeValidator:
    """Проверяет длительность выполнения привычки, она не должна превышать 2 минут."""

    def __init__(self, time_complete):
        self.time_complete = time_complete

    def __call__(self, habit):
        max_time = timedelta(seconds=120)
        if habit.get(self.time_complete) and habit.get(self.time_complete) > max_time:
            raise ValidationError(f"Выполнение не может длиться более 120 секунд")


class PleasantHabitValidator:
    """Проверят, что связанная привычка имеет признак приятной привычки."""

    def __init__(self, related_habit, pleasant_habit):
        self.related_habit = related_habit
        self.pleasant_habit = pleasant_habit

    def __call__(self, habit):
        if habit.get(self.related_habit) and not habit.get(self.pleasant_habit):
            raise ValidationError("Привычка не является приятной")


class FrequencyValidator:
    """Проверяет, является ли периодичность привычки корректной."""

    def __init__(self, frequency_habit):
        self.frequency_habit = frequency_habit

    def __call__(self, habit):
        if habit.get(self.frequency_habit) > 7:
            raise ValidationError(
                "Нельзя выполнять привычку реже,чем 1 раз в 7 дней."
            )


class AbsenceValidator:
    """Проверяет, если привычка имеет признак приятной, у нее не должно быть вознаграджения или связанной привычки"""

    def __init__(self, award, related_habit, pleasant_habit):
        self.award = award
        self.related_habit = related_habit
        self.pleasant_habit = pleasant_habit

    def __call__(self, habit):
        if habit.get(self.pleasant_habit) and habit.get(self.award) or habit.get(self.related_habit):
            raise ValidationError("Приятная привычка не должна иметь вознаграждения или связанную привычку.")
