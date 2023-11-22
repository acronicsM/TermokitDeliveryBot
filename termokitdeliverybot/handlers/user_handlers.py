from aiogram import Dispatcher
from aiogram.types import Message, ContentType

from termokitdeliverybot.keyboards.set_menu import drivers_menu


async def process_start_command(message: Message):
    await message.answer(text='/start')

# async def process_help_command(message: Message):
#     await message.answer(text=LEXICON_EN['/help'])


async def process_any_text(message: Message):
    await message.answer(text=message.text)


def register_user_handlers(dp: Dispatcher):
    # dp.message.register(process_start_command)
    # dp.register_message_handler(process_help_command, commands='help')
    # dp.message.register(process_any_text,  content_types=ContentType.TEXT)

    drivers_menu(dp)
