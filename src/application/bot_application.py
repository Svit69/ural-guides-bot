import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config.environment import EnvironmentSettings
from src.database.connection_factory import SqliteConnectionFactory
from src.database.schema_initializer import DatabaseSchemaInitializer
from src.handlers.admin_handler import AdminPanelHandler
from src.handlers.start_handler import StartCommandHandler
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
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
        admin_repository = AdminRepository(self.__connection_factory)
        post_repository = PostRepository(self.__connection_factory)
        user_repository = UserRepository(self.__connection_factory)
        StartCommandHandler(post_repository, user_repository).register_in_dispatcher(
            self.__dispatcher
        )
        AdminPanelHandler(
            admin_repository, post_repository, user_repository
        ).register_in_dispatcher(self.__dispatcher)

    def __initialize_database(self) -> None:
        DatabaseSchemaInitializer(self.__connection_factory).initialize_schema()
        AdminBootstrapper(AdminRepository(self.__connection_factory)).seed_initial_admins(
            self.__settings.initial_admin_ids
        )

    async def __start_polling(self) -> None:
        bot = Bot(
            token=self.__settings.telegram_bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        await self.__dispatcher.start_polling(bot)
