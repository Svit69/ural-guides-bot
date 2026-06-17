from src.config.environment import EnvironmentSettings
from src.database.connection_factory import SqliteConnectionFactory
from src.payments.city_payment_service import CityPaymentService
from src.payments.yookassa_gateway import YooKassaPaymentGateway
from src.payments.yookassa_settings import YooKassaSettings
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.city_payment_repository import CityPaymentRepository


class CityPaymentServiceFactory:
    def create(
        self, settings: EnvironmentSettings, connections: SqliteConnectionFactory
    ) -> CityPaymentService:
        payment_settings = YooKassaSettings(
            settings.yookassa_shop_id,
            settings.yookassa_secret_key,
            settings.viz_guide_price_rub,
            settings.yookassa_return_url,
            settings.city_guide_price_rub,
        )
        return CityPaymentService(
            payment_settings,
            YooKassaPaymentGateway(payment_settings),
            CityPaymentRepository(connections),
            CityAccessRepository(connections),
        )
