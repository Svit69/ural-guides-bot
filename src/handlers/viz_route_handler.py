from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import VIZ_FIFTH_POST_NUMBER, VIZ_FOURTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SEVENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_EIGHTH_POST_NUMBER
from src.guides.viz_posts import VIZ_NINTH_POST_NUMBER
from src.guides.viz_posts import VIZ_THIRD_POST_NUMBER


class VizRouteHandlerMixin:
    async def _send_viz_third_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_THIRD_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_THIRD
        )

    async def _send_viz_fourth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_FOURTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_FOURTH
        )

    async def _send_viz_fifth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_FIFTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_FIFTH
        )

    async def _send_viz_sixth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_SIXTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_SIXTH
        )

    async def _send_viz_seventh_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_SEVENTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_SEVENTH
        )

    async def _send_viz_eighth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_EIGHTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_EIGHTH
        )

    async def _send_viz_ninth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_NINTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_NINTH
        )

    async def _send_viz_post(
        self, callback: CallbackQuery, post_number: int, next_callback: str
    ) -> None:
        await callback.answer()
        if callback.message is None:
            return
        keyboard = GuideKeyboardFactory().build_viz_next_keyboard(next_callback)
        await self._post_sender.send_post(
            callback.message, self._posts.get_post(post_number), keyboard
        )
