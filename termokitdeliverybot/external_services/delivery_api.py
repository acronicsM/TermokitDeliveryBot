import aiohttp
import asyncio

from ..config_data.config import config


async def drivers_auth(driver_id):
    url = f'{config.api.url}/auth/registration'
    data_auth = {"id": driver_id,"name": "string","auth": False}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data_auth) as resp:
            if resp.status not in [200, 401]:
                return "Сервис временно не доступен, повторите команду позже"

            response = await resp.json()
            return response['description']
