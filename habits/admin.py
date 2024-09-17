from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "pleasant_habit",
        "related_habit",
        "frequency_habit",
        "award",
        "time_complete",
        "is_public",
    )
