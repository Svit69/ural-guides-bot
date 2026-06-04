import base64
import json
import urllib.request

from src.payments.yookassa_settings import YooKassaSettings


class YooKassaRequestBuilder:
    def __init__(self, settings: YooKassaSettings, api_url: str) -> None:
        self.__settings = settings
        self.__api_url = api_url

    def build(self, path: str, method: str, payload, idempotence_key: str | None):
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = urllib.request.Request(f"{self.__api_url}{path}", data=data, method=method)
        request.add_header("Authorization", f"Basic {self.__build_credentials()}")
        request.add_header("Content-Type", "application/json")
        if idempotence_key:
            request.add_header("Idempotence-Key", idempotence_key)
        return request

    def __build_credentials(self) -> str:
        raw_value = f"{self.__settings.shop_id}:{self.__settings.secret_key}".encode()
        return base64.b64encode(raw_value).decode()
