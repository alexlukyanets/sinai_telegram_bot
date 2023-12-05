from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegram_bot.bot.fsms.create_user import RegisterUserStates
from telegram_bot.bot.fsms.menu import MenuStates
from telegram_bot.bot.keyboards.default import request_contact
from telegram_bot.bot.keyboards.inline.menu import create_menu_markup
from telegram_bot.bot.keyboards.flex_keyboards import build_flex_keyboard
from telegram_bot.bot.use_case import CORE_USE_CASE


# from app.apps.core.telegram_bot.bot.fsms.create_user import RegisterUserStates
# from app.apps.core.telegram_bot.bot.fsms.menu import MenuStates
# from app.apps.core.telegram_bot.bot.keyboards.default import request_contact
# from app.apps.core.telegram_bot.bot.keyboards.inline.menu import create_menu_markup
# from app.apps.core.use_case import CORE_USE_CASE

async def handle_create_name(message: Message, state: FSMContext) -> None:
    await state.update_data({'name': message.text})
    await state.set_state(RegisterUserStates.waiting_for_phone_number)
    await message.answer('Відправте свій контакт', reply_markup=request_contact)


async def share_your_number(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await CORE_USE_CASE.register_sinai_user(
        name=data.get('name'),
        phone_number=message.contact.phone_number,
        telegram_id=message.from_user.id)
    menu_items, keyboard_type, message_reply = await CORE_USE_CASE.get_menu()
    await message.answer(f'Обирай категорію',
                         reply_markup=build_flex_keyboard(menu_items, keyboard_type))
    await state.set_state(MenuStates.waiting_for_choice)
