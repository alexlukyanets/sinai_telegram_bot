from typing import List
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def build_flex_keyboard(menu_items: List, keyboard_type: str):
    keyboard = {}
    for item in menu_items:
        row = item['position_in_row']
        text = item.get('text')
        callback_data = item.get('name_of_execution_function')

        if row in keyboard:
            if keyboard_type == 'inline':
                keyboard[row].append(InlineKeyboardButton(text=text, callback_data=callback_data))
                continue
            keyboard[row].append(KeyboardButton(text=text))
            continue

        if keyboard_type == 'inline':
            keyboard[row] = [InlineKeyboardButton(text=text, callback_data=callback_data)]
            continue
        keyboard[row] = [KeyboardButton(text=text)]

    if keyboard_type == 'reply':
        return ReplyKeyboardMarkup(
            keyboard=list(keyboard.values()),
            resize_keyboard=True,
            one_time_keyboard=True
        )
    elif keyboard_type == 'inline':
        return InlineKeyboardMarkup(inline_keyboard=list(keyboard.values()))
