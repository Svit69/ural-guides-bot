from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.feedback.admin_notifier import FeedbackAdminNotifier
from src.feedback.callbacks import FeedbackCallbackData
from src.feedback.feedback_payload import FeedbackPayloadBuilder
from src.feedback.feedback_preview_sender import FeedbackPreviewSender
from src.feedback.messages import FEEDBACK_EMPTY_TEXT, FEEDBACK_SENT_TEXT
from src.feedback.states import FeedbackStates
from src.handlers.feedback_edit_handler import FeedbackEditHandlerMixin
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository


class FeedbackHandler(FeedbackEditHandlerMixin):
    def __init__(self, admin_repository: AdminRepository, feedback_repository: FeedbackRepository) -> None:
        self.__feedback_repository = feedback_repository
        self.__notifier = FeedbackAdminNotifier(admin_repository)
        self.__payload_builder = FeedbackPayloadBuilder()
        self.__preview_sender = FeedbackPreviewSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__receive_feedback, FeedbackStates.waiting_for_feedback)
        dispatcher.callback_query.register(self.__send_feedback, F.data == FeedbackCallbackData.SEND_FEEDBACK)
        dispatcher.callback_query.register(self._edit_feedback, F.data == FeedbackCallbackData.EDIT_FEEDBACK)

    async def __receive_feedback(self, message: Message, state: FSMContext) -> None:
        payload = self.__payload_builder.build_payload(message)
        if self.__payload_builder.is_empty(payload):
            await message.answer(FEEDBACK_EMPTY_TEXT)
            return
        await state.update_data(feedback_payload=payload)
        await state.set_state(FeedbackStates.waiting_for_confirmation)
        await self.__preview_sender.send_preview(message, payload)

    async def __send_feedback(self, callback: CallbackQuery, state: FSMContext, bot: Bot) -> None:
        data = await state.get_data()
        payload = data.get("feedback_payload")
        if payload is None:
            await callback.answer(FEEDBACK_EMPTY_TEXT, show_alert=True)
            return
        self.__feedback_repository.save_feedback(payload)
        await self.__notifier.notify_admins(bot, payload)
        await state.clear()
        await callback.answer()
        if callback.message is not None:
            await callback.message.answer(FEEDBACK_SENT_TEXT)
