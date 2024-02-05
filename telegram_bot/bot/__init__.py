__all__ = ('register_user_commands', 'bot_commands', 'register_user_handlers',)

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from telegram_bot.models import MenuItem

from aiogram import Router, F
from aiogram.filters import CommandStart

from telegram_bot.bot.fsms.create_user import RegisterUserStates
from telegram_bot.bot.handlers.start_heandler import handle_start_command

from telegram_bot.bot.handlers.menu_hendler import menu_handler
from telegram_bot.bot.use_case import CORE_USE_CASE

router = Router()

router.message.register(handle_start_command, CommandStart())


for menu_text in MenuItem.objects.all().values_list('text', 'name_of_execution_function'):
    router.message.register(menu_handler, F.text == menu_text[0])
    router.callback_query.register(menu_handler, F.data == menu_text[1])
#
# router.callback_query.register(send_to_admins, F.data == 'send_to_admins')
