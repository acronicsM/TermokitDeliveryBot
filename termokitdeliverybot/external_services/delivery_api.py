import aiohttp
import asyncio

from ..config_data.config import config


async def drivers_auth(driver_id: int, full_name: str):
    url = f'{config.api.url}/auth/registration'
    data_auth = {"id": driver_id, "name": full_name, "auth": False}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data_auth) as resp:
            if resp.status not in [200, 401]:
                return True, await resp.text()

            response = await resp.json()
            return False, response['description']


async def driver_orders(driver_id: int):
    url = f'{config.api.url}/tg/{driver_id}/'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return True, []

            return False, await resp.json()
