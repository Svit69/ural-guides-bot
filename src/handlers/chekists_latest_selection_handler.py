from aiogram.types import CallbackQuery
from src.guides import chekists_posts as post
from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory


class ChekistsLatestSelectionHandlerMixin:
    async def _send_chekists_thirty_second_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRTY_SECOND
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTY_SECOND_POST_NUMBER, next_callback)

    async def _send_chekists_thirty_third_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRTY_THIRD
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTY_THIRD_POST_NUMBER, next_callback)

    async def _send_chekists_thirty_fourth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRTY_FOURTH
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTY_FOURTH_POST_NUMBER, next_callback)

    async def _send_chekists_thirty_fifth_post(self, callback: CallbackQuery) -> None:
        keyboard = GuideKeyboardFactory().build_chekists_finish_keyboard()
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTY_FIFTH_POST_NUMBER, keyboard=keyboard)
