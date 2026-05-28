from aiogram import Dispatcher

from src.config.environment import EnvironmentSettings
from src.database.connection_factory import SqliteConnectionFactory
from src.handlers.admin_handler import AdminPanelHandler
from src.handlers.route_navigation_handler import RouteNavigationHandler
from src.handlers.start_handler import StartCommandHandler
from src.handlers.subscription_handler import SubscriptionCheckHandler
from src.messages.post_provider import PostProvider
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.subscription.checker import ChannelSubscriptionChecker


class HandlerRegistrar:
    def __init__(
        self, settings: EnvironmentSettings, connections: SqliteConnectionFactory
    ) -> None:
        self.__settings = settings
        self.__connections = connections

    def register_handlers(self, dispatcher: Dispatcher) -> None:
        admin_repository = AdminRepository(self.__connections)
        media_repository = PostMediaRepository(self.__connections)
        post_repository = PostRepository(self.__connections)
        user_repository = UserRepository(self.__connections)
        checker = ChannelSubscriptionChecker(
            self.__settings.subscription_channel_username
        )
        post_provider = PostProvider(post_repository, media_repository)
        StartCommandHandler(
            post_repository, media_repository, user_repository
        ).register_in_dispatcher(dispatcher)
        SubscriptionCheckHandler(checker, post_provider).register_in_dispatcher(dispatcher)
        RouteNavigationHandler(post_provider).register_in_dispatcher(dispatcher)
        AdminPanelHandler(
            admin_repository, post_repository, media_repository, user_repository
        ).register_in_dispatcher(dispatcher)
