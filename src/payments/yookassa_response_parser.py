from src.payments.exceptions import PaymentGatewayError


class YooKassaResponseParser:
    def parse_confirmation_payment(self, result: dict[str, object]) -> dict[str, str]:
        try:
            return {
                "payment_id": str(result["id"]),
                "status": str(result["status"]),
                "confirmation_url": str(result["confirmation"]["confirmation_url"]),
            }
        except KeyError as error:
            message = "YooKassa response has no confirmation URL"
            raise PaymentGatewayError(message) from error
