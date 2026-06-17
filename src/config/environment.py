import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class EnvironmentSettings:
    telegram_bot_token: str
    database_path: str
    initial_admin_ids: tuple[int, ...]
    subscription_channel_username: str
    yookassa_shop_id: str
    yookassa_secret_key: str
    viz_guide_price_rub: str
    city_guide_price_rub: str
    yookassa_return_url: str

    @classmethod
    def load_from_environment(cls) -> "EnvironmentSettings":
        load_dotenv()
        token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        if not token:
            raise RuntimeError("Set TELEGRAM_BOT_TOKEN in environment or .env")
        admin_ids = os.getenv("ADMIN_TELEGRAM_IDS", "265485424")
        return cls(
            token,
            os.getenv("BOT_DATABASE_PATH", "bot_data.sqlite3"),
            cls.__parse_ids(admin_ids),
            os.getenv("SUBSCRIPTION_CHANNEL_USERNAME", "@nast_bar"),
            os.getenv("YOOKASSA_SHOP_ID", "").strip(),
            os.getenv("YOOKASSA_SECRET_KEY", "").strip(),
            os.getenv("VIZ_GUIDE_PRICE_RUB", "").strip(),
            os.getenv("CITY_GUIDE_PRICE_RUB", "").strip(),
            os.getenv("YOOKASSA_RETURN_URL", "https://t.me/nast_bar_bot").strip(),
        )

    @staticmethod
    def __parse_ids(raw_value: str) -> tuple[int, ...]:
        return tuple(
            int(value.strip()) for value in raw_value.split(",") if value.strip()
        )
