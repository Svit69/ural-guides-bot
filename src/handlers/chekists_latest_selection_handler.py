from aiogram.types import CallbackQuery
from src.guides import chekists_posts as post


class ChekistsLatestSelectionHandlerMixin:
    async def _send_chekists_thirty_second_post(self, callback: CallbackQuery) -> None:
        await self._send_chekists_next(callback, post.CHEKISTS_THIRTY_SECOND_POST_NUMBER)
