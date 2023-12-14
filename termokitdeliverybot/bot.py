'''
Main project file. Entry point.
'''

import asyncio
import logging

from aiogram import Bot, Dispatcher

# from config_data.config import Config, load_config
from config_data.config import config
from handlers.user_handlers import register_user_handlers
from keyboards.set_menu import set_drivers_menu


__version__ = "0.1.0"

# Initialize logger
logger = logging.getLogger(__name__)


# Registering all handlers
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)


# Function to configure and launch bot
async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # Print in console about starting bot
    logger.info('Starting bot...')

    # config: Config = load_config(r'.env')

    # Initializing bot and dispatcher
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='MarkdownV2')
    dp: Dispatcher = Dispatcher()

    dp.startup.register(set_drivers_menu)
    register_all_handlers(dp)
    
    # Start polling
    try:
        # Uncomment if want skip all updates from bot.
        # dp.skip_updates()
        await dp.start_polling(bot)
    except Exception:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot has been stopped!')
