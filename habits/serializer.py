from rest_framework import serializers
from .models import Habits
from .validators import (
    ChoiceRewardValidator,
    TimeValidator,
    PleasantHabitValidator,
    FrequencyValidator,
    AbsenceValidator,
)


class HabitsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Привычки."""
    class Meta:
        model = Habits
        fields = '__all__'
        validators = [
            ChoiceRewardValidator('related_habit','award'),
            TimeValidator('time_complete'),
            PleasantHabitValidator('related_habit', 'pleasant_habit'),
            FrequencyValidator('frequency_habit'),
            AbsenceValidator('award', 'related_habit', 'pleasant_habit'),
        ]