from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Надіслати контакт", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
help_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/help")]], resize_keyboard=True,
)
