from aiogram.types import Message

from telegram_bot.bot.keyboards.flex_keyboards import build_flex_keyboard
from telegram_bot.bot.use_case import CORE_USE_CASE


async def create_greeting(username, first_name, last_name):
    greeting_parts = []

    if first_name:
        greeting_parts.append(first_name)

    if last_name:
        greeting_parts.append(last_name)

    if not first_name and not last_name:
        greeting_parts.append(f"(@{username})")

    full_name = " ".join(greeting_parts)

    greeting = f"Вітаємо, {full_name}!" if full_name else "Вітаємо!"

    return greeting


async def handle_start_command(message: Message) -> None:
    _, is_new = await CORE_USE_CASE.register_bot_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        language_code=message.from_user.language_code
    )

    menu_items, keyboard_type, _, _ = await CORE_USE_CASE.get_menu()

    greeting = await create_greeting(message.from_user.username, message.from_user.first_name, message.from_user.last_name)
    await message.answer(greeting,
                         reply_markup=build_flex_keyboard(menu_items, keyboard_type))
