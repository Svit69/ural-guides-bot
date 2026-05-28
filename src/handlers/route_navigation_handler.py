from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.messages.default_posts import THIRD_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.route_navigation.callbacks import RouteNavigationCallbackData
from src.services.post_sender import TelegramPostSender


class RouteNavigationHandler:
    def __init__(self, post_provider: PostProvider) -> None:
        self.__post_provider = post_provider
        self.__post_sender = TelegramPostSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__send_third_post,
            F.data == RouteNavigationCallbackData.THIRD_POST,
        )

    async def __send_third_post(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        await self.__post_sender.send_post(
            callback.message, self.__post_provider.get_post(THIRD_POST_NUMBER)
        )
