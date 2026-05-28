import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config.environment import EnvironmentSettings
from src.handlers.start_handler import StartCommandHandler


class BotApplication:
    def __init__(self, settings: EnvironmentSettings) -> None:
        self.__settings = settings
        self.__dispatcher = Dispatcher()
        self.__register_handlers()

    def run_polling(self) -> None:
        asyncio.run(self.__start_polling())

    def __register_handlers(self) -> None:
        StartCommandHandler().register_in_dispatcher(self.__dispatcher)

    async def __start_polling(self) -> None:
        bot = Bot(
            token=self.__settings.telegram_bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        await self.__dispatcher.start_polling(bot)
