from aiogram import Bot, types
from aiogram.enums import ParseMode

# Initialize your bot
bot = Bot(token='6829218306:AAHMHRHlUkpv3OAMu1e1OGxOf-Cn-dVfQGg')

# Your bold text
bold_text = "This is *bold* text using Markdown."


# Send a message with Markdown formatting
async def send_message_with_markdown():
    await bot.send_message(chat_id=306382573, text=bold_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_with_markdown())
