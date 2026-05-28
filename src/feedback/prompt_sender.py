from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.feedback.messages import FEEDBACK_PROMPT_TEXT
from src.feedback.states import FeedbackStates


class FeedbackPromptSender:
    async def send_feedback_prompt(self, message: Message, state: FSMContext) -> None:
        await state.set_state(FeedbackStates.waiting_for_feedback)
        await message.answer(FEEDBACK_PROMPT_TEXT)
