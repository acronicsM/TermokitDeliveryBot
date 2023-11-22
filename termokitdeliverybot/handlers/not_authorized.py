from aiogram.types import Message


async def sign_up_answer(message: Message):
    await message.answer(text='Вы не авторизованы, зарегистрируйтесь для дальнейшей работы')
