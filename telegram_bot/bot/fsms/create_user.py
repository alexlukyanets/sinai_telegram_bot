from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()


class RegisterUserStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone_number = State()