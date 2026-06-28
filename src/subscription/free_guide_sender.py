from aiogram.types import CallbackQuery

from src.guides.chekists_posts import CHEKISTS_FIRST_POST_NUMBER
from src.guides.guide_ids import GUIDE_CHEKISTS
from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.messages.default_posts import SECOND_POST_NUMBER, THIRD_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.route_navigation.keyboards import RouteNavigationKeyboardFactory
from src.services.post_sender import TelegramPostSender
from src.subscription.callbacks import SubscriptionCallbackData


class FreeGuideSender:
    def __init__(self, posts: PostProvider) -> None:
        self.__guide_keyboards = GuideKeyboardFactory()
        self.__post_sender = TelegramPostSender()
        self.__posts = posts
        self.__route_keyboards = RouteNavigationKeyboardFactory()

    async def send_guide(self, callback: CallbackQuery) -> None:
        guide_id = SubscriptionCallbackData.parse_guide_id(callback.data or "")
        if guide_id == GUIDE_CHEKISTS:
            await self.__post_sender.send_post(
                callback.message,
                self.__posts.get_post(CHEKISTS_FIRST_POST_NUMBER),
                self.__guide_keyboards.build_chekists_next_keyboard(
                    GuideCallbackData.CHEKISTS_NEXT_AFTER_FIRST
                ),
            )
            return
        await self.__post_sender.send_post(
            callback.message,
            self.__posts.get_post(SECOND_POST_NUMBER),
            self.__route_keyboards.build_next_post_keyboard(THIRD_POST_NUMBER),
        )
