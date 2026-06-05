from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.viz_posts import VIZ_FIFTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SEVENTEENTH_POST_NUMBER
from src.guides.viz_posts import VIZ_SIXTEENTH_POST_NUMBER


class VizFinalRouteHandlerMixin:
    async def _send_viz_fifteenth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_FIFTEENTH_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_FIFTEENTH,
        )

    async def _send_viz_sixteenth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_SIXTEENTH_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_SIXTEENTH,
        )

    async def _send_viz_seventeenth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_SEVENTEENTH_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_SEVENTEENTH,
        )
