import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class EnvironmentSettings:
    telegram_bot_token: str

    @classmethod
    def load_from_environment(cls) -> "EnvironmentSettings":
        load_dotenv()
        token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        if not token:
            raise RuntimeError("Set TELEGRAM_BOT_TOKEN in environment or .env")
        return cls(telegram_bot_token=token)
