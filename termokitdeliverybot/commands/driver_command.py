from aiogram.utils.formatting import Text
from aiogram.utils.markdown import bold
from aiogram.types import Message

# from ..models.db import db
from ..handlers.api_error import api_error_message
from ..keyboards.keyboard import order_keyboard
from ..external_services.delivery_api import drivers_auth, driver_orders


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
    error, orders_list = await driver_orders(driver_id=message.from_user.id)

    if error:
        await api_error_message(message)
        return

    if not orders_list:
        await message.answer(text=f'Новых доставок нет')

    for order in orders_list:
        order_number, address, comment = order['orde_1c_number'], order['address'], order['comment']
        order_number, text = bold(order_number), Text(f'{address}\n{comment}').as_markdown()

        await message.answer(
            text=f'{order_number}\n{text}',
            reply_markup=order_keyboard(driver_id=message.from_user.id, order_id=order['id']),
        )


async def delivery(message: Message):
    await message.answer(text='ТЕСТ')


async def help(message: Message):
    await message.answer(text='ТЕСТ')


async def registration(message: Message):
    error, msg = await drivers_auth(driver_id=message.from_user.id, full_name=message.from_user.full_name)

    if error:
        await api_error_message(message)
        return

    await message.answer(text=msg)
