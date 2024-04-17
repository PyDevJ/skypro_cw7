import requests
from celery import shared_task

from config import settings
from habits.models import Habit


@shared_task
def habit_operate():
    """Функция формирования сообщений о привычках для пользователей."""
    habits = Habit.objects.all()

    for habit in habits:
        if not habit.is_nice:
            text = f"Я буду {habit.action} в {habit.time.strftime('%H:%M')} в {habit.place}."
            if habit.associated_hab:
                text += f" Затем я сделаю: {habit.associated_hab.action}."
            if habit.reward:
                text += f" Я получу: {habit.reward}."
            print(text)
            # send_message(text, habit.user.chat_id)


def send_message(text, user_chat_id):
    """Функция отправки сообщения в чат-бот Telegram."""
    url = 'https://api.telegram.org/bot'
    token = settings.TELEBOT_KEY
    requests.post(
        url=f"{url}{token}/sendMessage",
        data={
            "chat_id": user_chat_id,
            "text": text
        }
    )
