from aiogram import Bot, Dispatcher, F
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.types import CallbackQuery

from src.messages.default_posts import SECOND_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.services.post_sender import TelegramPostSender
from src.subscription.callbacks import SubscriptionCallbackData
from src.subscription.checker import ChannelSubscriptionChecker
from src.subscription.messages import (
    SUBSCRIPTION_CHECK_ERROR_TEXT,
    SUBSCRIPTION_CONFIRMED_TEXT,
    SUBSCRIPTION_REQUIRED_TEXT,
)


class SubscriptionCheckHandler:
    def __init__(self, checker: ChannelSubscriptionChecker, posts: PostProvider) -> None:
        self.__checker = checker
        self.__post_provider = posts
        self.__post_sender = TelegramPostSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__check_subscription,
            F.data == SubscriptionCallbackData.CHECK_SUBSCRIPTION,
        )

    async def __check_subscription(self, callback: CallbackQuery, bot: Bot) -> None:
        try:
            is_subscribed = await self.__checker.has_active_subscription(
                bot, callback.from_user.id
            )
        except (TelegramBadRequest, TelegramForbiddenError):
            await callback.answer(SUBSCRIPTION_CHECK_ERROR_TEXT, show_alert=True)
            return
        answer_text = (
            SUBSCRIPTION_CONFIRMED_TEXT
            if is_subscribed
            else SUBSCRIPTION_REQUIRED_TEXT
        )
        await callback.answer(answer_text, show_alert=True)
        if is_subscribed and callback.message is not None:
            await self.__post_sender.send_post(
                callback.message, self.__post_provider.get_post(SECOND_POST_NUMBER)
            )
