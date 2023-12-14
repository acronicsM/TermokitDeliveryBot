from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


class DeliveryAPI:
    url = 'http://127.0.0.1:8000'


@dataclass
class Config:
    tg_bot: TgBot
    api: DeliveryAPI


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)
    tg_bot = TgBot(token=env('BOT_TOKEN'),
                 admin_ids=list(map(int, env.list('ADMIN_IDS'))))
    return Config(tg_bot=tg_bot, api=DeliveryAPI())


config = load_config('.env')
