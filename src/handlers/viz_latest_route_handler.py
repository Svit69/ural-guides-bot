from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.viz_post_numbers import VIZ_TWENTY_FOURTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_SECOND_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_THIRD_POST_NUMBER


class VizLatestRouteHandlerMixin:
    async def _send_viz_twenty_second_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_TWENTY_SECOND_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_SECOND,
        )

    async def _send_viz_twenty_third_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_TWENTY_THIRD_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_THIRD,
        )

    async def _send_viz_twenty_fourth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_TWENTY_FOURTH_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_FOURTH,
        )
