from aiogram.types import Message

from src.subscription.keyboards import SubscriptionKeyboardFactory
from src.subscription.messages import SUBSCRIPTION_PROMPT_TEXT
from src.text_formatting.telegram_formatter import TelegramTextFormatter


class SubscriptionPromptSender:
    def __init__(self) -> None:
        self.__formatter = TelegramTextFormatter()
        self.__keyboard_factory = SubscriptionKeyboardFactory()

    async def send_subscription_prompt(self, message: Message, guide_id: str = "big_konny") -> None:
        await message.answer(
            self.__formatter.format_text(SUBSCRIPTION_PROMPT_TEXT),
            reply_markup=self.__keyboard_factory.build_subscription_keyboard(guide_id),
            disable_web_page_preview=True,
        )
