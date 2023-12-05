from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def create_menu_markup(menu_items):
    # keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # buttons = []
    # menu_items.sort(key=lambda x: x[3])
    # for item in menu_items:
    #     callback = item[0]
    #     if not callback:
    #         callback = 'None'
    #     buttons.append(InlineKeyboardButton(text=item[1], callback_data=callback))
    # keyboard.row(*buttons, width=1)
    # return keyboard.as_markup()
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Про церкву🤵"),
                KeyboardButton(text="Соц мережі👪"),
            ],
            [
                KeyboardButton(text="Соціальні проекти🍂"),
                KeyboardButton(text="Розклад Служінь🏐"),
            ],
            [
                KeyboardButton(text="Зворотній зв'зок‍🎓"),
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
