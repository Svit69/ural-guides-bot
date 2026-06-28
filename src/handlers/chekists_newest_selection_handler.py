from aiogram.types import CallbackQuery
from src.guides import chekists_posts as post
from src.guides.callbacks import GuideCallbackData


class ChekistsNewestSelectionHandlerMixin:
    async def _send_chekists_twenty_first_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_FIRST
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_FIRST_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_second_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_SECOND
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_SECOND_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_third_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_THIRD
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_THIRD_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_fourth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_FOURTH
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_FOURTH_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_fifth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_FIFTH
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_FIFTH_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_sixth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_SIXTH
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_SIXTH_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_seventh_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_SEVENTH
        keyboard = self._build_idol_next_keyboard(6, next_callback)
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_SEVENTH_POST_NUMBER, keyboard=keyboard)

    async def _send_chekists_twenty_eighth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_EIGHTH
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_EIGHTH_POST_NUMBER, next_callback)

    async def _send_chekists_twenty_ninth_post(self, callback: CallbackQuery) -> None:
        next_callback = GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_NINTH
        keyboard = self._build_idol_next_keyboard(7, next_callback)
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_NINTH_POST_NUMBER, keyboard=keyboard)

    async def _send_chekists_thirtieth_post(self, callback: CallbackQuery) -> None:
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTIETH_POST_NUMBER)
