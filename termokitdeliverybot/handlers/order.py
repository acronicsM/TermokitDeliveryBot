from aiogram.types import CallbackQuery, Message
from aiogram.utils.formatting import Text
from aiogram.utils.markdown import bold

from ..filters.callbackdata import Order
# from ..models.db import db
from ..keyboards.keyboard import item_keyboard
from .not_authorized import sign_up_answer


async def select_order(call: CallbackQuery, callback_data: Order):
    # _id, _type = callback_data.vacancy_id, callback_data.vacancy_type
    #
    # await call.message.answer(text='Выберите GPT провайдера',
    #                           reply_markup=get_gpt_keyboard(_id, _type),
    #                           )

    chauffeur, order_id = call.from_user.id, callback_data.order_id
    # if not db.get(call.from_user.id):
    #     await sign_up_answer(call.message)
    #     return
    #
    # if db.get(call.from_user.id).get(order_id):
    #     await order_items(call.message, chauffeur, order_id)
    # else:
    #     await order_not_found(call.message, order_id)
    await order_not_found(call.message, order_id)




async def order_items(message: Message, chauffeur, order_id):
    pass
    # for item in db[chauffeur][order_id]['items']:
    #     item_id, name = bold(item['id']), Text(item['name']).as_markdown()
    #
    #     count, unit, price, item_sum = item['count'], item['unit'], item['price'], item['sum']
    #     discount, bonus = item['discount'], item['bonus']
    #
    #     formula = Text(f'{count}{unit} * {price} - {discount}% - {bonus}А = ').as_markdown() + bold(item_sum) + '₽'
    #
    #     await message.answer(text=f'{item_id}\n{name}\n{formula}',
    #                          reply_markup=item_keyboard(order_id, item_id),
    #                          )


async def order_not_found(message: Message, order_id):
    await message.answer(text=f'У вас не найдено заказа с идентификатором {order_id}')


async def select_orderAPP(call: CallbackQuery, callback_data: Order):
    chauffeur, order_id = call.from_user.id, callback_data.order_id
    # if not db.get(call.from_user.id):
    #     await sign_up_answer(call.message)
    #     return
    #
    # if db.get(call.from_user.id).get(order_id):
    #     await order_items(call.message, chauffeur, order_id)
    # else:
    #     await order_not_found(call.message, order_id)
    await order_not_found(call.message, order_id)


async def order_APP(message: Message, chauffeur, order_id):
    # for item in db[chauffeur][order_id]['items']:
    #     item_id, name = bold(item['id']), Text(item['name']).as_markdown()
    #
    #     count, unit, price, item_sum = item['count'], item['unit'], item['price'], item['sum']
    #     discount, bonus = item['discount'], item['bonus']
    #
    #     formula = Text(f'{count}{unit} * {price} - {discount}% - {bonus}А = ').as_markdown() + bold(item_sum) + '₽'
    #
    #     await message.answer(text=f'{item_id}\n{name}\n{formula}',
    #                          reply_markup=item_keyboard(order_id, item_id),
    #                          )
    pass
