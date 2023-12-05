from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from telegram_bot.models import MenuLevel

storage = MemoryStorage()

levels = MenuLevel.objects.all().values_list('level_text_id')


class MenuStates(StatesGroup):
    waiting_for_choice = State()
