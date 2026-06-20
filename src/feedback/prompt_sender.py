from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.feedback.keyboards import FeedbackKeyboardFactory
from src.feedback.messages import FEEDBACK_PROMPT_TEXT
from src.feedback.states import FeedbackStates


class FeedbackPromptSender:
    def __init__(self) -> None:
        self.__keyboards = FeedbackKeyboardFactory()

    async def send_feedback_prompt(
        self, message: Message, state: FSMContext, text: str = FEEDBACK_PROMPT_TEXT
    ) -> None:
        await state.set_state(FeedbackStates.waiting_for_feedback)
        await message.answer(text, reply_markup=self.__keyboards.build_leave_later_keyboard())
