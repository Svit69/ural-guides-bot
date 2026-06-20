from src.payments.payment_gateway import PaymentGateway
from src.payments.viz_purchase_validator import VizPurchaseValidator
from src.payments.yookassa_settings import YooKassaSettings
from src.repositories.viz_access_repository import VizAccessRepository
from src.repositories.viz_payment_repository import VizPaymentRepository

class VizPaymentService:
    def __init__(
        self,
        settings: YooKassaSettings,
        gateway: PaymentGateway,
        repository: VizPaymentRepository,
        access_repository: VizAccessRepository,
    ) -> None:
        self.__settings = settings
        self.__gateway = gateway
        self.__repository = repository
        self.__access_repository = access_repository
        self.__validator = VizPurchaseValidator(settings)

    def is_configured(self) -> bool:
        return self.__settings.is_configured()

    def get_price_rub(self) -> str:
        return self.__settings.viz_price_rub

    def has_local_access(self, user_id: int) -> bool:
        return self.__access_repository.has_access(user_id)

    async def get_or_create_payment(self, user_id: int) -> dict[str, object]:
        stored = self.__repository.get_payment(user_id)
        if stored and stored["status"] in {"pending", "waiting_for_capture", "succeeded"}:
            return stored
        payment = await self.__gateway.create_viz_payment(user_id)
        self.__repository.save_payment(user_id, payment)
        return payment

    async def has_paid_access(self, user_id: int) -> bool:
        if self.has_local_access(user_id):
            return True
        stored = self.__repository.get_payment(user_id)
        if stored is None:
            return False
        payment = await self.__gateway.get_payment(str(stored["payment_id"]))
        status = str(payment.get("status", ""))
        self.__repository.update_status(user_id, status)
        has_access = status == "succeeded" and self.__validator.matches_purchase(payment, user_id)
        if has_access:
            self.__access_repository.grant_access(user_id, str(stored["payment_id"]))
        return has_access
