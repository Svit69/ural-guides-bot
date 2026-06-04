import json
import logging
import urllib.error

from src.payments.exceptions import PaymentGatewayError


class YooKassaErrorHandler:
    def raise_http_error(self, error: urllib.error.HTTPError) -> None:
        response_body = error.read().decode("utf-8", errors="replace")
        logging.error("YooKassa HTTP %s: %s", error.code, response_body)
        try:
            response = json.loads(response_body)
            reason = str(response.get("description") or response.get("code") or "")
        except ValueError:
            reason = ""
        raise PaymentGatewayError(f"YooKassa HTTP {error.code}", reason) from error
