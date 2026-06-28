from aiogram.types import CallbackQuery
from src.guides.callbacks import GuideCallbackData
from src.guides.chekists_keyboards import ChekistsKeyboardFactory
from src.guides.guide_ids import GUIDE_CHEKISTS
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.chekists_posts import CHEKISTS_EIGHTH_POST_NUMBER, CHEKISTS_ELEVENTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_FIFTH_POST_NUMBER, CHEKISTS_FOURTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_NINTH_POST_NUMBER, CHEKISTS_SECOND_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_SEVENTH_POST_NUMBER, CHEKISTS_SIXTH_POST_NUMBER
from src.guides.chekists_posts import CHEKISTS_TENTH_POST_NUMBER, CHEKISTS_THIRD_POST_NUMBER
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender
class ChekistsSelectionHandlerMixin:
    def _init_chekists_sender(self) -> None:
        self.__chekists_keyboards = GuideKeyboardFactory()
        self.__chekists_special_keyboards = ChekistsKeyboardFactory()
        self.__chekists_post_sender = TelegramPostSender()
    async def _select_chekists(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is not None:
            await SubscriptionPromptSender().send_subscription_prompt(callback.message, GUIDE_CHEKISTS)
    async def _answer_chekists_next(self, callback: CallbackQuery) -> None:
        await callback.answer("Скоро добавлю следующую точку маршрута.", show_alert=True)
    async def _send_chekists_second_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_SECOND_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_SECOND)
    async def _send_chekists_third_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_THIRD_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRD)
    async def _send_chekists_fourth_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_FOURTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_FOURTH)
    async def _send_chekists_fifth_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_FIFTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_FIFTH)
    async def _send_chekists_sixth_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_SIXTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_SIXTH)
    async def _send_chekists_seventh_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_SEVENTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_SEVENTH)
    async def _send_chekists_eighth_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_EIGHTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_EIGHTH)
    async def _send_chekists_ninth_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_NINTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_NINTH)
    async def _send_chekists_tenth_post(self, callback: CallbackQuery) -> None:
        await self.__send_next(callback, CHEKISTS_TENTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_TENTH)
    async def _send_chekists_eleventh_post(self, callback: CallbackQuery) -> None:
        keyboard = self.__chekists_special_keyboards.build_find_all_idols_keyboard()
        await self.__send_next(callback, CHEKISTS_ELEVENTH_POST_NUMBER, keyboard=keyboard)
    async def __send_next(self, callback, post_number, next_callback=None, keyboard=None):
        await callback.answer()
        if callback.message is None:
            return
        keyboard = keyboard or self.__chekists_keyboards.build_chekists_next_keyboard(next_callback)
        await self.__chekists_post_sender.send_post(callback.message, self._posts.get_post(post_number), keyboard)
