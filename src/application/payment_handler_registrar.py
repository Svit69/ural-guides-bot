from aiogram import Dispatcher

from src.config.environment import EnvironmentSettings
from src.database.connection_factory import SqliteConnectionFactory
from src.handlers.city_payment_handler import CityPaymentHandler
from src.handlers.viz_payment_handler import VizPaymentHandler
from src.messages.post_provider import PostProvider
from src.payments.city_payment_factory import CityPaymentServiceFactory
from src.payments.viz_payment_factory import VizPaymentServiceFactory
from src.repositories.admin_repository import AdminRepository


class PaymentHandlerRegistrar:
    def __init__(self, settings: EnvironmentSettings, connections: SqliteConnectionFactory) -> None:
        self.__settings = settings
        self.__connections = connections

    def register(
        self, dispatcher: Dispatcher, posts: PostProvider, admins: AdminRepository
    ) -> None:
        viz_payments = VizPaymentServiceFactory().create(self.__settings, self.__connections)
        city_payments = CityPaymentServiceFactory().create(self.__settings, self.__connections)
        VizPaymentHandler(viz_payments, posts, admins).register_in_dispatcher(dispatcher)
        CityPaymentHandler(city_payments, posts, admins).register_in_dispatcher(dispatcher)
