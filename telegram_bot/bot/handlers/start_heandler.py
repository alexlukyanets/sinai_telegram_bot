from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegram_bot.bot.fsms.create_user import RegisterUserStates
from telegram_bot.bot.fsms.menu import MenuStates
from telegram_bot.bot.keyboards.inline.menu import create_menu_markup
from telegram_bot.bot.keyboards.flex_keyboards import build_flex_keyboard
from telegram_bot.bot.use_case import CORE_USE_CASE


async def handle_start_command(message: Message, state: FSMContext) -> None:
    if message.from_user is None:
        return

    _, is_new = await CORE_USE_CASE.register_bot_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        language_code=message.from_user.language_code
    )
    if not is_new:
        await state.set_state(MenuStates.waiting_for_choice)
        menu_items, keyboard_type, _ = await CORE_USE_CASE.get_menu()
        await message.answer(f'Обирай категорію',
                             reply_markup=build_flex_keyboard(menu_items, keyboard_type))
        return

    await state.set_state(RegisterUserStates.waiting_for_name)
    await message.answer("Як до вас можно звертатися?")
