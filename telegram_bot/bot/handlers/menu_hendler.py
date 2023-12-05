from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegram_bot.bot.fsms.menu import MenuStates
from telegram_bot.bot.keyboards.flex_keyboards import build_flex_keyboard
from telegram_bot.bot.use_case import CORE_USE_CASE


async def menu_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    menu_items, keyboard_type, message_reply = await CORE_USE_CASE.get_menu(message.text, current_state)
    await message.answer(message_reply,
                         parse_mode=ParseMode.MARKDOWN,
                         reply_markup=build_flex_keyboard(menu_items, keyboard_type))
