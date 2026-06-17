import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config.environment import EnvironmentSettings
from src.database.city_payment_schema_initializer import CityPaymentSchemaInitializer
from src.database.connection_factory import SqliteConnectionFactory
from src.database.schema_initializer import DatabaseSchemaInitializer
from src.database.viz_payment_schema_initializer import VizPaymentSchemaInitializer
from src.application.handler_registrar import HandlerRegistrar
from src.repositories.admin_repository import AdminRepository
from src.services.admin_bootstrapper import AdminBootstrapper


class BotApplication:
    def __init__(self, settings: EnvironmentSettings) -> None:
        self.__settings = settings
        self.__dispatcher = Dispatcher()
        self.__connection_factory = SqliteConnectionFactory(settings.database_path)
        self.__initialize_database()
        self.__register_handlers()

    def run_polling(self) -> None:
        asyncio.run(self.__start_polling())

    def __register_handlers(self) -> None:
        HandlerRegistrar(self.__settings, self.__connection_factory).register_handlers(
            self.__dispatcher
        )

    def __initialize_database(self) -> None:
        DatabaseSchemaInitializer(self.__connection_factory).initialize_schema()
        VizPaymentSchemaInitializer(self.__connection_factory).initialize_schema()
        CityPaymentSchemaInitializer(self.__connection_factory).initialize_schema()
        AdminBootstrapper(AdminRepository(self.__connection_factory)).seed_initial_admins(
            self.__settings.initial_admin_ids
        )

    async def __start_polling(self) -> None:
        bot = Bot(
            token=self.__settings.telegram_bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        await self.__dispatcher.start_polling(bot)
