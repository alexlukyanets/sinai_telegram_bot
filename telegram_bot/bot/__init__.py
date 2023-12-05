__all__ = ('register_user_commands', 'bot_commands', 'register_user_handlers',)

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
django.setup()

from telegram_bot.models import MenuItem

from aiogram import Router, F
from aiogram.filters import CommandStart

from telegram_bot.bot.fsms.create_user import RegisterUserStates
from telegram_bot.bot.fsms.menu import MenuStates
from telegram_bot.bot.handlers.register_user_heandler import share_your_number, handle_create_name
from telegram_bot.bot.handlers.start_heandler import handle_start_command

from telegram_bot.bot.handlers.menu_hendler import menu_handler

router = Router()

router.message.register(handle_start_command, CommandStart())
router.message.register(handle_create_name, RegisterUserStates.waiting_for_name)
router.message.register(share_your_number, RegisterUserStates.waiting_for_phone_number)

for menu_text in MenuItem.objects.all().values_list('text'):
    router.message.register(menu_handler, F.text == menu_text[0])
# router.callback_query.register(handle_appointment, F.data == 'make_appointment')
#
# router.callback_query.register(send_to_admins, F.data == 'send_to_admins')
