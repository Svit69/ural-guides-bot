from aiogram.types import CallbackQuery
from src.guides import chekists_posts as post


class ChekistsNewestSelectionHandlerMixin:
    async def _send_chekists_twenty_first_post(self, callback: CallbackQuery) -> None:
        await self._send_chekists_next(callback, post.CHEKISTS_TWENTY_FIRST_POST_NUMBER)
