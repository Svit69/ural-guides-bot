from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_post_numbers import VIZ_TWENTY_FIFTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_FOURTH_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_SECOND_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_THIRD_POST_NUMBER
from src.guides.viz_post_numbers import VIZ_TWENTY_SIXTH_POST_NUMBER


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

    async def _send_viz_twenty_fifth_post(self, callback: CallbackQuery) -> None:
        await self._send_viz_post(
            callback,
            VIZ_TWENTY_FIFTH_POST_NUMBER,
            GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_FIFTH,
        )

    async def _send_viz_twenty_sixth_post(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        await self._post_sender.send_post(
            callback.message,
            self._posts.get_post(VIZ_TWENTY_SIXTH_POST_NUMBER),
            GuideKeyboardFactory().build_viz_finish_keyboard(),
        )
