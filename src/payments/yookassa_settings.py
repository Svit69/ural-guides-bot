from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class YooKassaSettings:
    shop_id: str
    secret_key: str
    viz_price_rub: str
    return_url: str
    city_price_rub: str = ""

    def is_configured(self) -> bool:
        try:
            return bool(
                self.shop_id
                and self.secret_key
                and self.return_url
                and Decimal(self.viz_price_rub) > 0
            )
        except InvalidOperation:
            return False

    def is_city_configured(self) -> bool:
        try:
            return bool(
                self.shop_id
                and self.secret_key
                and self.return_url
                and Decimal(self.city_price_rub) > 0
            )
        except InvalidOperation:
            return False
