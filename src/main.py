from src.application.bot_application import BotApplication
from src.config.environment import EnvironmentSettings


def run_telegram_guide_bot() -> None:
    settings = EnvironmentSettings.load_from_environment()
    application = BotApplication(settings)
    application.run_polling()


if __name__ == "__main__":
    run_telegram_guide_bot()
