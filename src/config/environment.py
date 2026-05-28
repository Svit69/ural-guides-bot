import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class EnvironmentSettings:
    telegram_bot_token: str
    database_path: str
    initial_admin_ids: tuple[int, ...]
    subscription_channel_username: str

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
        )

    @staticmethod
    def __parse_ids(raw_value: str) -> tuple[int, ...]:
        return tuple(
            int(value.strip()) for value in raw_value.split(",") if value.strip()
        )
