from aiogram.filters.callback_data import CallbackData


class Order(CallbackData, prefix='order'):
    order_id: str


class Item(CallbackData, prefix='item'):
    order_id: str
    item_id: str
    operand: str
