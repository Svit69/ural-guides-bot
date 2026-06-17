import asyncio
from pathlib import Path

from src.database.city_payment_schema_initializer import CityPaymentSchemaInitializer
from src.database.connection_factory import SqliteConnectionFactory
from src.payments.city_payment_service import CityPaymentService
from src.payments.payment_gateway import PaymentGateway
from src.payments.yookassa_settings import YooKassaSettings
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.city_payment_repository import CityPaymentRepository


class FakeCityGateway(PaymentGateway):
    async def create_viz_payment(self, user_id: int) -> dict[str, str]:
        return {}

    async def create_city_payment(self, user_id: int) -> dict[str, str]:
        return {"payment_id": "city-1", "status": "pending", "confirmation_url": "https://pay"}

    async def get_payment(self, payment_id: str) -> dict[str, object]:
        return {
            "id": payment_id,
            "status": "succeeded",
            "amount": {"value": "700.00", "currency": "RUB"},
            "metadata": {"guide": "city_walk", "telegram_user_id": "1"},
        }


def test_creates_payment_and_grants_city_access(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    CityPaymentSchemaInitializer(connections).initialize_schema()
    settings = YooKassaSettings("shop", "secret", "500.00", "https://t.me/bot", "700.00")
    service = CityPaymentService(
        settings, FakeCityGateway(), CityPaymentRepository(connections),
        CityAccessRepository(connections)
    )

    payment = asyncio.run(service.get_or_create_payment(1))
    has_access = asyncio.run(service.has_paid_access(1))

    assert payment["confirmation_url"] == "https://pay"
    assert has_access is True
    assert service.has_local_access(1) is True
