from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.viz_posts import VIZ_EIGHTH_POST_NUMBER, VIZ_NINTH_POST_NUMBER
from src.guides.viz_posts import VIZ_TENTH_POST_NUMBER


class VizLaterRouteHandlerMixin:
    async def _send_viz_eighth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_EIGHTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_EIGHTH
        )

    async def _send_viz_ninth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_NINTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_NINTH
        )

    async def _send_viz_tenth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback, VIZ_TENTH_POST_NUMBER, GuideCallbackData.VIZ_NEXT_AFTER_TENTH
        )
