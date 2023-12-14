from aiogram.utils.formatting import Text
from aiogram.utils.markdown import bold
from aiogram.types import Message

# from ..models.db import db
from ..handlers.not_authorized import sign_up_answer
from ..keyboards.keyboard import order_keyboard
from ..external_services.delivery_api import drivers_auth


async def deliveries(message: Message):
    pass
    # chauffeur = db.get(message.from_user.id)
    #
    # if not chauffeur:
    #     await sign_up_answer(message)
    #     return
    #
    # for order_id, order in chauffeur.items():
    #     order_number, address, comment = order['id'], order['address'], order['comment']
    #     order_number, text = bold(order_number), Text(f'{address}\n{comment}').as_markdown()
    #
    #     await message.answer(text=f'{order_number}\n{text}',
    #                          reply_markup=order_keyboard(order_id),
    #                          )


async def delivery(message: Message):
    await message.answer(text='ТЕСТ')


async def help(message: Message):
    await message.answer(text='ТЕСТ')


async def registration(message: Message):
    await message.answer(text=await drivers_auth(driver_id=message.from_user.id))
