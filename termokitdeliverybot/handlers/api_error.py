from aiogram.types import Message


async def api_error_message(message: Message):
    await message.answer(text="Сервис временно не доступен, повторите команду позже")
