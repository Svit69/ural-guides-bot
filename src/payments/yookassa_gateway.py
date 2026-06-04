import asyncio
import json
import logging
import urllib.error
import urllib.request
import uuid

from src.payments.exceptions import PaymentGatewayError
from src.payments.payment_gateway import PaymentGateway
from src.payments.yookassa_error_handler import YooKassaErrorHandler
from src.payments.yookassa_request_builder import YooKassaRequestBuilder
from src.payments.yookassa_settings import YooKassaSettings


class YooKassaPaymentGateway(PaymentGateway):
    __api_url = "https://api.yookassa.ru/v3/payments"
    def __init__(self, settings: YooKassaSettings) -> None:
        self.__settings = settings
        self.__error_handler = YooKassaErrorHandler()
        self.__request_builder = YooKassaRequestBuilder(settings, self.__api_url)

    async def create_viz_payment(self, user_id: int) -> dict[str, str]:
        payload = {
            "amount": {"value": self.__settings.viz_price_rub, "currency": "RUB"},
            "confirmation": {"type": "redirect", "return_url": self.__settings.return_url},
            "capture": True,
            "description": "Гайд по ВИЗу",
            "metadata": {"guide": "viz", "telegram_user_id": str(user_id)},
        }
        result = await asyncio.to_thread(self.__request, "", "POST", payload, str(uuid.uuid4()))
        try:
            return {
                "payment_id": str(result["id"]),
                "status": str(result["status"]),
                "confirmation_url": str(result["confirmation"]["confirmation_url"]),
            }
        except KeyError as error:
            raise PaymentGatewayError("YooKassa response has no confirmation URL") from error

    async def get_payment(self, payment_id: str) -> dict[str, object]:
        return await asyncio.to_thread(self.__request, f"/{payment_id}", "GET", None, None)
    def __request(self, path: str, method: str, payload, idempotence_key: str | None):
        request = self.__request_builder.build(path, method, payload, idempotence_key)
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            self.__error_handler.raise_http_error(error)
        except (urllib.error.URLError, ValueError, KeyError) as error:
            logging.exception("YooKassa request failed")
            raise PaymentGatewayError("YooKassa request failed") from error
