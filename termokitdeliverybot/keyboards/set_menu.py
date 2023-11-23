from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from aiogram.filters import Command

from termokitdeliverybot.commands import driver_command as dc
from termokitdeliverybot.filters.callbackdata import Order, OrderAPP
from termokitdeliverybot.handlers.order import select_order, select_orderAPP


def drivers_menu(dp: Dispatcher):
    dp.callback_query.register(select_order, Order.filter())
    dp.callback_query.register(select_orderAPP, OrderAPP.filter())

    dp.message.register(dc.deliveries, Command(commands=['deliveries']))
    dp.message.register(dc.delivery, Command(commands=['delivery']))
    dp.message.register(dc.help, Command(commands=['help']))
    dp.message.register(dc.registration, Command(commands=['registration']))


async def set_drivers_menu(bot:Bot):
    bot_commands = [
        BotCommand(command='/deliveries', description='Мои доставки'),
        BotCommand(command='/delivery', description='Доставка по номеру'),
        BotCommand(command='/help', description='Помощь'),
        BotCommand(command='/registration', description='Регистрация'),
    ]

    await bot.set_my_commands(bot_commands)

