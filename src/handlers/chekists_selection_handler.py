from aiogram.types import CallbackQuery

from src.guides.guide_ids import GUIDE_CHEKISTS
from src.subscription.prompt_sender import SubscriptionPromptSender


class ChekistsSelectionHandlerMixin:
    async def _select_chekists(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is not None:
            await SubscriptionPromptSender().send_subscription_prompt(
                callback.message, GUIDE_CHEKISTS
            )

    async def _answer_chekists_next(self, callback: CallbackQuery) -> None:
        await callback.answer(
            "Скоро добавлю следующую точку маршрута.", show_alert=True
        )
