import asyncio
from pathlib import Path

from src.database.connection_factory import SqliteConnectionFactory
from src.database.viz_payment_schema_initializer import VizPaymentSchemaInitializer
from src.payments.payment_gateway import PaymentGateway
from src.payments.keyboards import VizPaymentKeyboardFactory
from src.payments.messages import build_viz_payment_prompt
from src.payments.viz_payment_service import VizPaymentService
from src.payments.yookassa_settings import YooKassaSettings
from src.repositories.viz_payment_repository import VizPaymentRepository


class FakePaymentGateway(PaymentGateway):
    async def create_viz_payment(self, user_id: int) -> dict[str, str]:
        return {"payment_id": "payment-1", "status": "pending", "confirmation_url": "https://pay"}

    async def get_payment(self, payment_id: str) -> dict[str, object]:
        return {
            "id": payment_id,
            "status": "succeeded",
            "amount": {"value": "500.00", "currency": "RUB"},
            "metadata": {"guide": "viz", "telegram_user_id": "1"},
        }


def test_creates_payment_and_grants_paid_viz_access(tmp_path: Path) -> None:
    connections = SqliteConnectionFactory(str(tmp_path / "bot.sqlite3"))
    VizPaymentSchemaInitializer(connections).initialize_schema()
    settings = YooKassaSettings("shop", "secret", "500.00", "https://t.me/bot")
    repository = VizPaymentRepository(connections)
    service = VizPaymentService(settings, FakePaymentGateway(), repository)

    payment = asyncio.run(service.get_or_create_payment(1))
    has_access = asyncio.run(service.has_paid_access(1))

    assert payment["confirmation_url"] == "https://pay"
    assert has_access is True
    assert repository.get_payment(1)["status"] == "succeeded"


def test_rejects_unconfigured_payment_settings() -> None:
    settings = YooKassaSettings("", "", "", "")

    assert settings.is_configured() is False


def test_builds_viz_payment_keyboard() -> None:
    keyboard = VizPaymentKeyboardFactory().build_payment_keyboard("https://pay")

    assert keyboard.inline_keyboard[0][0].url == "https://pay"
    assert keyboard.inline_keyboard[1][0].callback_data == "guide:viz:payment:check"
    assert "500.00 ₽" in build_viz_payment_prompt("500.00")
