from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.subscription.callbacks import SubscriptionCallbackData


class SubscriptionKeyboardFactory:
    def build_subscription_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Открыть канал", url="https://t.me/nast_bar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Проверить подписку",
                        callback_data=SubscriptionCallbackData.CHECK_SUBSCRIPTION,
                    )
                ],
            ]
        )
