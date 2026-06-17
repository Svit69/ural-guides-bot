from decimal import Decimal

from src.payments.yookassa_settings import YooKassaSettings


class CityPurchaseValidator:
    def __init__(self, settings: YooKassaSettings) -> None:
        self.__settings = settings

    def matches_purchase(self, payment: dict[str, object], user_id: int) -> bool:
        metadata = dict(payment.get("metadata") or {})
        amount = dict(payment.get("amount") or {})
        return (
            metadata.get("guide") == "city_walk"
            and metadata.get("telegram_user_id") == str(user_id)
            and amount.get("currency") == "RUB"
            and Decimal(str(amount.get("value", "0")))
            == Decimal(self.__settings.city_price_rub)
        )
