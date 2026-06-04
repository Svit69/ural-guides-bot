from decimal import Decimal

from src.payments.payment_gateway import PaymentGateway
from src.payments.yookassa_settings import YooKassaSettings
from src.repositories.viz_payment_repository import VizPaymentRepository


class VizPaymentService:
    def __init__(
        self,
        settings: YooKassaSettings,
        gateway: PaymentGateway,
        repository: VizPaymentRepository,
    ) -> None:
        self.__settings = settings
        self.__gateway = gateway
        self.__repository = repository

    def is_configured(self) -> bool:
        return self.__settings.is_configured()

    def get_price_rub(self) -> str:
        return self.__settings.viz_price_rub

    async def get_or_create_payment(self, user_id: int) -> dict[str, object]:
        stored = self.__repository.get_payment(user_id)
        if stored and stored["status"] in {"pending", "waiting_for_capture", "succeeded"}:
            return stored
        payment = await self.__gateway.create_viz_payment(user_id)
        self.__repository.save_payment(user_id, payment)
        return payment

    async def has_paid_access(self, user_id: int) -> bool:
        stored = self.__repository.get_payment(user_id)
        if stored is None:
            return False
        payment = await self.__gateway.get_payment(str(stored["payment_id"]))
        status = str(payment.get("status", ""))
        self.__repository.update_status(user_id, status)
        return status == "succeeded" and self.__matches_purchase(payment, user_id)

    def __matches_purchase(self, payment: dict[str, object], user_id: int) -> bool:
        metadata = dict(payment.get("metadata") or {})
        amount = dict(payment.get("amount") or {})
        return (
            metadata.get("guide") == "viz"
            and metadata.get("telegram_user_id") == str(user_id)
            and amount.get("currency") == "RUB"
            and Decimal(str(amount.get("value", "0"))) == Decimal(self.__settings.viz_price_rub)
        )
