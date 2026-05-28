from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.feedback.prompt_sender import FeedbackPromptSender
from src.messages.default_posts import FINAL_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.route_navigation.callbacks import RouteNavigationCallbackData
from src.route_navigation.keyboards import RouteNavigationKeyboardFactory
from src.route_navigation.next_post_resolver import NextPostResolver
from src.services.post_sender import TelegramPostSender


class RouteNavigationHandler:
    def __init__(self, post_provider: PostProvider) -> None:
        self.__callbacks = RouteNavigationCallbackData()
        self.__keyboard_factory = RouteNavigationKeyboardFactory()
        self.__next_post_resolver = NextPostResolver()
        self.__post_provider = post_provider
        self.__post_sender = TelegramPostSender()
        self.__feedback_prompt_sender = FeedbackPromptSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__send_route_post,
            F.data.startswith(RouteNavigationCallbackData.PREFIX),
        )

    async def __send_route_post(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        post_number = self.__callbacks.parse_post_number(callback.data or "")
        if callback.message is None or post_number is None:
            return
        await self.__post_sender.send_post(
            callback.message,
            self.__post_provider.get_post(post_number),
            self.__build_next_keyboard(post_number),
        )
        if post_number == FINAL_POST_NUMBER:
            await self.__feedback_prompt_sender.send_feedback_prompt(
                callback.message, state
            )

    def __build_next_keyboard(self, current_post_number: int):
        next_post = self.__next_post_resolver.resolve_next_post(current_post_number)
        return self.__keyboard_factory.build_next_post_keyboard(next_post) if next_post else None
