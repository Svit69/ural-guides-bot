from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.guide_ids import GUIDE_BIG_KONNY
from src.handlers.chekists_selection_handler import ChekistsSelectionHandlerMixin
from src.guides.viz_posts import VIZ_SECOND_POST_NUMBER
from src.handlers.viz_callback_registrar import VizCallbackRegistrar
from src.handlers.viz_feedback_finish_handler import VizFeedbackFinishHandlerMixin
from src.handlers.viz_final_route_handler import VizFinalRouteHandlerMixin
from src.handlers.viz_later_route_handler import VizLaterRouteHandlerMixin
from src.handlers.viz_latest_route_handler import VizLatestRouteHandlerMixin
from src.handlers.viz_newest_route_handler import VizNewestRouteHandlerMixin
from src.handlers.viz_route_handler import VizRouteHandlerMixin
from src.messages.post_provider import PostProvider
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender
class GuideSelectionHandler(ChekistsSelectionHandlerMixin, VizRouteHandlerMixin, VizLaterRouteHandlerMixin, VizFinalRouteHandlerMixin, VizNewestRouteHandlerMixin, VizLatestRouteHandlerMixin, VizFeedbackFinishHandlerMixin):
    def __init__(self, posts: PostProvider) -> None:
        self._posts = posts
        self._init_chekists_sender()
        self._post_sender = TelegramPostSender()
        self.__keyboards = GuideKeyboardFactory()
        self.__route_registrar = VizCallbackRegistrar()
        self.__subscription_prompt = SubscriptionPromptSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__select_big_konny, F.data == GuideCallbackData.SELECT_BIG_KONNY)
        dispatcher.callback_query.register(self._select_chekists, F.data == GuideCallbackData.SELECT_CHEKISTS)
        dispatcher.callback_query.register(self.__send_viz_second_post, F.data == GuideCallbackData.VIZ_NEXT)
        dispatcher.callback_query.register(self._send_chekists_second_post, F.data == GuideCallbackData.CHEKISTS_NEXT_AFTER_FIRST)
        dispatcher.callback_query.register(self._send_chekists_third_post, F.data == GuideCallbackData.CHEKISTS_NEXT_AFTER_SECOND)
        dispatcher.callback_query.register(self._send_chekists_fourth_post, F.data == GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRD)
        dispatcher.callback_query.register(self._answer_chekists_next, F.data == GuideCallbackData.CHEKISTS_NEXT)
        self.__route_registrar.register_route_callbacks(dispatcher, self)
        dispatcher.callback_query.register(self._start_viz_feedback, F.data == GuideCallbackData.FINISH_VIZ)

    async def __select_big_konny(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is not None:
            await self.__subscription_prompt.send_subscription_prompt(callback.message, GUIDE_BIG_KONNY)
    async def __send_viz_second_post(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None: return
        await self._post_sender.send_post(
            callback.message,
            self._posts.get_post(VIZ_SECOND_POST_NUMBER),
            self.__keyboards.build_viz_next_keyboard(GuideCallbackData.VIZ_NEXT_AFTER_SECOND),
        )
