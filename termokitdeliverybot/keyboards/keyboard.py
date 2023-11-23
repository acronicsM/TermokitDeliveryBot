from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from ..filters.callbackdata import Order, OrderAPP, Item


def order_keyboard(order_id):
    web_app = WebAppInfo(url='site_url')

    builder = InlineKeyboardBuilder()
    builder.button(text='📥 Открыть', callback_data=Order(order_id=order_id))
    builder.button(text='📥 APP', callback_data=OrderAPP(order_id=order_id))
    builder.button(text='📥 site', web_app=web_app)

    return builder.as_markup()


def item_keyboard(order_id, item_id):
    builder = InlineKeyboardBuilder()

    builder.button(text='➖ 1',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='➕ 1',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='❌ Убрать всё',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='🧮 Указать кол',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.adjust(2)

    return builder.as_markup()
