import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.web.settings")
django.setup()

from aiogram import Router
from aiogram.filters import CommandStart

from telegram_bot.fsms.create_user import RegisterUserStates
from telegram_bot.fsms.menu import MenuStates
from telegram_bot.handlers.register_user_heandler import share_your_number, handle_create_name
from telegram_bot.handlers.start_heandler import handle_start_command

# TG_TOKEN = os.getenv('TG_TOKEN')

router = Router()

router.message.register(handle_start_command, CommandStart())
router.message.register(handle_create_name, RegisterUserStates.waiting_for_name)
router.message.register(share_your_number, RegisterUserStates.waiting_for_phone_number)
# router.message.register(send_to_admins_comments, MenuStates.waiting_for_comment)
# router.callback_query.register(handle_appointment, F.data == 'make_appointment')
# router.callback_query.register(add_comment, F.data == 'add_comment')
# router.callback_query.register(send_to_admins, F.data == 'send_to_admins')
# router.callback_query.register(back_to_main_menu, F.data == 'back_to_main_menu')
