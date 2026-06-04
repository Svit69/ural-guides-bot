from src.config.environment import EnvironmentSettings
from src.database.connection_factory import SqliteConnectionFactory
from src.payments.viz_payment_service import VizPaymentService
from src.payments.yookassa_gateway import YooKassaPaymentGateway
from src.payments.yookassa_settings import YooKassaSettings
from src.repositories.viz_payment_repository import VizPaymentRepository


class VizPaymentServiceFactory:
    def create(
        self,
        settings: EnvironmentSettings,
        connections: SqliteConnectionFactory,
    ) -> VizPaymentService:
        payment_settings = YooKassaSettings(
            settings.yookassa_shop_id,
            settings.yookassa_secret_key,
            settings.viz_guide_price_rub,
            settings.yookassa_return_url,
        )
        return VizPaymentService(
            payment_settings,
            YooKassaPaymentGateway(payment_settings),
            VizPaymentRepository(connections),
        )
