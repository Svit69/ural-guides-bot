from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import VIZ_SECOND_POST_NUMBER
from src.handlers.viz_later_route_handler import VizLaterRouteHandlerMixin
from src.handlers.viz_route_handler import VizRouteHandlerMixin
from src.messages.post_provider import PostProvider
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender


class GuideSelectionHandler(VizRouteHandlerMixin, VizLaterRouteHandlerMixin):
    def __init__(self, posts: PostProvider) -> None:
        self._posts = posts
        self._post_sender = TelegramPostSender()
        self.__keyboards = GuideKeyboardFactory()
        self.__subscription_prompt = SubscriptionPromptSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__select_big_konny, F.data == GuideCallbackData.SELECT_BIG_KONNY)
        dispatcher.callback_query.register(self.__send_viz_second_post, F.data == GuideCallbackData.VIZ_NEXT)
        dispatcher.callback_query.register(self._send_viz_third_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SECOND)
        dispatcher.callback_query.register(self._send_viz_fourth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_THIRD)
        dispatcher.callback_query.register(self._send_viz_fifth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_FOURTH)
        dispatcher.callback_query.register(self._send_viz_sixth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_FIFTH)
        dispatcher.callback_query.register(self._send_viz_seventh_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SIXTH)
        dispatcher.callback_query.register(self._send_viz_eighth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SEVENTH)
        dispatcher.callback_query.register(self._send_viz_ninth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_EIGHTH)
        dispatcher.callback_query.register(self._send_viz_tenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_NINTH)
        dispatcher.callback_query.register(self._send_viz_eleventh_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TENTH)
        dispatcher.callback_query.register(self._send_viz_twelfth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_ELEVENTH)
        dispatcher.callback_query.register(self._send_viz_thirteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWELFTH)
        dispatcher.callback_query.register(self.__handle_viz_next, F.data == GuideCallbackData.VIZ_NEXT_AFTER_THIRTEENTH)

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
