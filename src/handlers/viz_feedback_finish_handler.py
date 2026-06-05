from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.feedback.prompt_sender import FeedbackPromptSender


class VizFeedbackFinishHandlerMixin:
    async def _start_viz_feedback(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if callback.message is not None:
            await FeedbackPromptSender().send_feedback_prompt(callback.message, state)
