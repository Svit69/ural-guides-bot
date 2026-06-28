from aiogram.types import CallbackQuery
from src.guides import chekists_posts as post
from src.guides.callbacks import GuideCallbackData


class ChekistsLateSelectionHandlerMixin:
    async def _send_chekists_tenth_post(self, callback: CallbackQuery) -> None:
        await self._send_chekists_next(
            callback, post.CHEKISTS_TENTH_POST_NUMBER, GuideCallbackData.CHEKISTS_NEXT_AFTER_TENTH
        )

    async def _send_chekists_eleventh_post(self, callback: CallbackQuery) -> None:
        keyboard = self._build_find_all_idols_keyboard()
        await self._send_chekists_next(callback, post.CHEKISTS_ELEVENTH_POST_NUMBER, keyboard=keyboard)

    async def _send_chekists_twelfth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWELFTH
        await self._send_chekists_next(callback, post.CHEKISTS_TWELFTH_POST_NUMBER, next_callback)

    async def _send_chekists_thirteenth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRTEENTH
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTEENTH_POST_NUMBER, next_callback)

    async def _send_chekists_fourteenth_post(self, callback: CallbackQuery) -> None:
        await self._send_chekists_next(callback, post.CHEKISTS_FOURTEENTH_POST_NUMBER)
