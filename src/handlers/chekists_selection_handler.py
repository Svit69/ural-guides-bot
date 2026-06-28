from aiogram.types import CallbackQuery
from src.guides.chekists_posts import CHEKISTS_FOURTH_POST_NUMBER, CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_THIRD_POST_NUMBER
from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.guide_ids import GUIDE_CHEKISTS
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender

class ChekistsSelectionHandlerMixin:
    def _init_chekists_sender(self) -> None:
        self.__chekists_keyboards = GuideKeyboardFactory()
        self.__chekists_post_sender = TelegramPostSender()

    async def _select_chekists(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is not None:
            await SubscriptionPromptSender().send_subscription_prompt(
                callback.message, GUIDE_CHEKISTS
            )

    async def _answer_chekists_next(self, callback: CallbackQuery) -> None:
        await callback.answer("Скоро добавлю следующую точку маршрута.", show_alert=True)

    async def _send_chekists_second_post(self, callback: CallbackQuery) -> None:
        await self.__send_chekists_post(
            callback, CHEKISTS_SECOND_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_SECOND
        )

    async def _send_chekists_third_post(self, callback: CallbackQuery) -> None:
        await self.__send_chekists_post(
            callback, CHEKISTS_THIRD_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRD
        )

    async def _send_chekists_fourth_post(self, callback: CallbackQuery) -> None:
        await self.__send_chekists_post(callback, CHEKISTS_FOURTH_POST_NUMBER)

    async def __send_chekists_post(
        self, callback: CallbackQuery, post_number: int, next_callback: str | None = None
    ) -> None:
        await callback.answer()
        if callback.message is None:
            return
        keyboard = self.__chekists_keyboards.build_chekists_next_keyboard(next_callback) if next_callback else self.__chekists_keyboards.build_chekists_next_keyboard()
        await self.__chekists_post_sender.send_post(
            callback.message,
            self._posts.get_post(post_number),
            keyboard,
        )
