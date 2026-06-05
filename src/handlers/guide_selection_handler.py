from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import VIZ_SECOND_POST_NUMBER
from src.handlers.viz_callback_registrar import VizCallbackRegistrar
from src.handlers.viz_final_route_handler import VizFinalRouteHandlerMixin
from src.handlers.viz_later_route_handler import VizLaterRouteHandlerMixin
from src.handlers.viz_route_handler import VizRouteHandlerMixin
from src.messages.post_provider import PostProvider
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender


class GuideSelectionHandler(
    VizRouteHandlerMixin, VizLaterRouteHandlerMixin, VizFinalRouteHandlerMixin
):
    def __init__(self, posts: PostProvider) -> None:
        self._posts = posts
        self._post_sender = TelegramPostSender()
        self.__keyboards = GuideKeyboardFactory()
        self.__route_registrar = VizCallbackRegistrar()
        self.__subscription_prompt = SubscriptionPromptSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__select_big_konny, F.data == GuideCallbackData.SELECT_BIG_KONNY)
        dispatcher.callback_query.register(self.__send_viz_second_post, F.data == GuideCallbackData.VIZ_NEXT)
        self.__route_registrar.register_route_callbacks(dispatcher, self)
        dispatcher.callback_query.register(self.__handle_viz_next, F.data == GuideCallbackData.VIZ_NEXT_AFTER_EIGHTEENTH)

    async def __select_big_konny(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is not None:
            await self.__subscription_prompt.send_subscription_prompt(callback.message)

    async def __send_viz_second_post(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        await self._post_sender.send_post(
            callback.message,
            self._posts.get_post(VIZ_SECOND_POST_NUMBER),
            self.__keyboards.build_viz_next_keyboard(GuideCallbackData.VIZ_NEXT_AFTER_SECOND),
        )

    async def __handle_viz_next(self, callback: CallbackQuery) -> None:
        await callback.answer("Следующий пост ВИЗа пока не добавлен.", show_alert=True)
