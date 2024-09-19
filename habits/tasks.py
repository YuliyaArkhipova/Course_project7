import datetime
from celery import shared_task

from habits.models import Habits
from habits.services import send_telegram_message


@shared_task
def send_reminder_habit():
    """Периодическая задача по отправке в телеграм напоминания о привычке"""
    habits = Habits.objects.all()
    current_date = datetime.datetime.now()
    for habit in habits:
        if habit.time == current_date:
            tg_chat = habit.user.telegram_id
            message = f"Я буду {habit.action} в {habit.time} {habit.place}."
            send_telegram_message(tg_chat, message)
