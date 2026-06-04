from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER, VIZ_SECOND_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender


class GuideSelectionHandler:
    def __init__(self, posts: PostProvider) -> None:
        self.__posts = posts
        self.__post_sender = TelegramPostSender()
        self.__keyboards = GuideKeyboardFactory()
        self.__subscription_prompt = SubscriptionPromptSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__select_viz, F.data == GuideCallbackData.SELECT_VIZ)
        dispatcher.callback_query.register(self.__select_big_konny, F.data == GuideCallbackData.SELECT_BIG_KONNY)
        dispatcher.callback_query.register(self.__send_viz_second_post, F.data == GuideCallbackData.VIZ_NEXT)
        dispatcher.callback_query.register(self.__handle_viz_next, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SECOND)

    async def __select_viz(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        await self.__post_sender.send_post(
            callback.message,
            self.__posts.get_post(VIZ_FIRST_POST_NUMBER),
            self.__keyboards.build_viz_next_keyboard(),
        )

    async def __select_big_konny(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is not None:
            await self.__subscription_prompt.send_subscription_prompt(callback.message)

    async def __send_viz_second_post(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        await self.__post_sender.send_post(
            callback.message,
            self.__posts.get_post(VIZ_SECOND_POST_NUMBER),
            self.__keyboards.build_viz_next_keyboard(GuideCallbackData.VIZ_NEXT_AFTER_SECOND),
        )

    async def __handle_viz_next(self, callback: CallbackQuery) -> None:
        await callback.answer("Следующий пост ВИЗа пока не добавлен.", show_alert=True)
