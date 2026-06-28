from aiogram import Dispatcher

from src.config.environment import EnvironmentSettings
from src.database.connection_factory import SqliteConnectionFactory
from src.application.repository_bundle import RepositoryBundle
from src.handlers.admin_handler import AdminPanelHandler
from src.handlers.guide_selection_handler import GuideSelectionHandler
from src.handlers.route_navigation_handler import RouteNavigationHandler
from src.handlers.subscription_handler import SubscriptionCheckHandler
from src.application.payment_handler_registrar import PaymentHandlerRegistrar
from src.application.user_interaction_registrar import UserInteractionRegistrar
from src.subscription.checker import ChannelSubscriptionChecker


class HandlerRegistrar:
    def __init__(self, settings: EnvironmentSettings, connections: SqliteConnectionFactory) -> None:
        self.__settings = settings
        self.__connections = connections

    def register_handlers(self, dispatcher: Dispatcher) -> None:
        repositories = RepositoryBundle(self.__connections)
        UserInteractionRegistrar(self.__settings).register(
            dispatcher, repositories.build_user_context()
        )
        GuideSelectionHandler(repositories.post_provider).register_in_dispatcher(dispatcher)
        PaymentHandlerRegistrar(self.__settings, self.__connections).register(
            dispatcher, repositories.post_provider, repositories.admins
        )
        checker = ChannelSubscriptionChecker(self.__settings.subscription_channel_username)
        SubscriptionCheckHandler(checker, repositories.post_provider).register_in_dispatcher(dispatcher)
        RouteNavigationHandler(repositories.post_provider).register_in_dispatcher(dispatcher)
        AdminPanelHandler(
            repositories.admins,
            repositories.feedback,
            repositories.posts,
            repositories.media,
            repositories.users,
            repositories.viz_access,
            repositories.city_access,
            repositories.guide_visibility,
        ).register_in_dispatcher(dispatcher)
