from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.feedback.feedback_payload import FeedbackPayloadBuilder
from src.feedback.feedback_preview_sender import FeedbackPreviewSender
from src.feedback.messages import FEEDBACK_EMPTY_TEXT
from src.feedback.states import FeedbackStates


class FeedbackMessageHandler:
    def __init__(self) -> None:
        self.__payload_builder = FeedbackPayloadBuilder()
        self.__preview_sender = FeedbackPreviewSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(
            self.__receive_feedback, FeedbackStates.waiting_for_feedback
        )

    async def __receive_feedback(self, message: Message, state: FSMContext) -> None:
        payload = self.__payload_builder.build_payload(message)
        if self.__payload_builder.is_empty(payload):
            await message.answer(FEEDBACK_EMPTY_TEXT)
            return
        await state.update_data(feedback_payload=payload)
        await state.set_state(FeedbackStates.waiting_for_confirmation)
        await self.__preview_sender.send_preview(message, payload)
