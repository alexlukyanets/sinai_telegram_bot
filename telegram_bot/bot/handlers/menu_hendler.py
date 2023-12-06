from aiogram.enums import ParseMode

from aiogram.types import Message

from telegram_bot.bot.keyboards.flex_keyboards import build_flex_keyboard

from telegram_bot.bot.use_case import CORE_USE_CASE


async def menu_handler(message: Message) -> None:
    menu_reply_mode = True
    try:
        menu_extractor = message.text
    except AttributeError:
        menu_reply_mode = False
        menu_extractor = message.data
    menu_items, keyboard_type, message_reply = await CORE_USE_CASE.get_menu(menu_extractor)
    if not menu_reply_mode and keyboard_type == 'reply':

        await message.bot.send_message(message.from_user.id, message_reply, parse_mode=ParseMode.MARKDOWN_V2,
                                       reply_markup=build_flex_keyboard(menu_items, keyboard_type))

        await message.answer()

    await message.answer(message_reply,
                         parse_mode=ParseMode.MARKDOWN_V2,
                         reply_markup=build_flex_keyboard(menu_items, keyboard_type))
