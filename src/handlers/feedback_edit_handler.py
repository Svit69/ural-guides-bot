from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.feedback.messages import FEEDBACK_EDIT_TEXT
from src.feedback.states import FeedbackStates


class FeedbackEditHandlerMixin:
    async def _edit_feedback(self, callback: CallbackQuery, state: FSMContext) -> None:
        await state.update_data(feedback_payload=None)
        await state.set_state(FeedbackStates.waiting_for_feedback)
        await callback.answer()
        if callback.message is not None:
            await callback.message.answer(FEEDBACK_EDIT_TEXT)
