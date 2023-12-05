from typing import List
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def build_flex_keyboard(menu_items: List, keyboard_type: str):
    keyboard = {}
    for item in menu_items:
        row = item['position_in_row']
        if row in keyboard:
            keyboard[row].append(KeyboardButton(text=item.get('text')))
            continue
        keyboard[row] = [KeyboardButton(text=item.get('text'))]

    if keyboard_type == 'reply':
        return ReplyKeyboardMarkup(
            keyboard=list(keyboard.values()),
            resize_keyboard=True,
            one_time_keyboard=True
        )
