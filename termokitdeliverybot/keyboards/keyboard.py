from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..filters.callbackdata import Order, Item


def order_keyboard(order_id):
    builder = InlineKeyboardBuilder()
    builder.button(text='📥 Открыть', callback_data=Order(order_id=order_id))

    return builder.as_markup()


def item_keyboard(order_id, item_id):
    builder = InlineKeyboardBuilder()
    builder.button(text='➖ Убрать 1 еденицу',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='❌ Убрать всё',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='➕ Добавить 1 едницу',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='➖➖ Убрать X едениц',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )

    builder.button(text='➕➕ Добавить X едениц',
                   callback_data=Item(order_id=order_id, item_id=item_id, operand='minus'),
                   )


    return builder.as_markup()