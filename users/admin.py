from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Пользователя."""
    list_display = (
        "pk",
        "email",
        "phone",
        "avatar",
        "telegram_id",
    )
