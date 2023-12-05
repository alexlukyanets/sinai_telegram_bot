from typing import Final

from aiogram.fsm.context import FSMContext

from telegram_bot.bot.fsms.menu import MenuStates
from telegram_bot.models import MenuItem, TelegramUser, DataBotText, SinaiUser, MenuLevel


# The `UseCase` classes are used to separate the business logic from the rest of the code.
# Also, because of this, we can easily use the same business logic in different places.
# For example, in the telegram_bot and in the web application.

# The main reason to use classes instead of functions is that
# the `UseCase` classes may depend on different services.


# Define a synchronous function to get menu items


class CoreUseCase:
    @staticmethod
    async def register_bot_user(
            user_id: int,
            username: str | None,
            first_name: str | None,
            last_name: str | None,
            language_code: str | None) -> tuple[TelegramUser, bool]:
        return await TelegramUser.objects.aget_or_create(
            tg_user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language_code=language_code)

    @classmethod
    async def register_sinai_user(cls,
                                  name: str,
                                  phone_number: str,
                                  telegram_id: int) -> tuple[TelegramUser, bool]:
        telegram_user = await TelegramUser.objects.aget(tg_user_id=telegram_id)
        return await SinaiUser.objects.aget_or_create(
            phone_number=phone_number,
            name=name,
            telegram_user=telegram_user)

    @staticmethod
    async def get_menu(menu_item_text=None, state: FSMContext = None):
        message_reply = 'Обирай Категорію'
        if not menu_item_text:

            menu_items = MenuItem.objects.filter(level__parent__isnull=True). \
                order_by('position_in_row', 'position_in_col')
        else:
            menu_item = await MenuItem.objects.aget(text=menu_item_text)
            menu_items = MenuItem.objects.filter(level__menu_level_id=menu_item.menu_reply_id).order_by(
                'position_in_row', 'position_in_col')
            if menu_item.text_reply:
                message_reply = menu_item.text_reply

        keyboard_type = None
        keyboard_menu_items = []
        async for menu_item in menu_items:
            if not keyboard_type:
                level = await MenuLevel.objects.aget(menu_level_id=menu_item.level_id)
                keyboard_type = level.keyboard_type
            keyboard_menu_items.append({'text': menu_item.text,
                                        'position_in_row': menu_item.position_in_row,
                                        'position_in_col': menu_item.position_in_col,
                                        'name_of_execution_function': menu_item.name_of_execution_function})
        return keyboard_menu_items, keyboard_type, message_reply

    @staticmethod
    async def select_admin_ids():
        user_ids = []
        async for user_id in TelegramUser.objects.filter(is_admin=True).values_list('user_id'):
            user_ids.append(user_id[0])
        return user_ids

    @staticmethod
    async def select_text_by_text_id(text_id) -> str:
        text = await DataBotText.objects.aget(id_value=text_id)
        if not text:
            raise RuntimeError('Unable to find by text_id')
        return text.text


CORE_USE_CASE: Final[CoreUseCase] = CoreUseCase()
