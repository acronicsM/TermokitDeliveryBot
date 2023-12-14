from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from ..filters.callbackdata import Order
from ..config_data.config import config


def order_keyboard(driver_id, order_id):

    # url = f'{config.api.url}/tg/{driver_id}/orders/{order_id}/cart'
    url = f'https://www.termokit.ru/tg/{driver_id}/orders/{order_id}/cart'

    web_app = WebAppInfo(url=url)

    builder = InlineKeyboardBuilder()
    builder.button(text='🧺 Открыть', web_app=web_app)
    builder.button(text='📥 Доставить', callback_data=Order(order_id=order_id))

    return builder.as_markup()
