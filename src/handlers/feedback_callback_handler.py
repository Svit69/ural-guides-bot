from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from src.feedback.admin_notifier import FeedbackAdminNotifier
from src.feedback.callbacks import FeedbackCallbackData
from src.feedback.completion_sender import FeedbackCompletionSender
from src.feedback.messages import FEEDBACK_EMPTY_TEXT
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository
from src.services.guide_list_sender import GuideListSender

class FeedbackCallbackHandler:
    def __init__(
        self,
        admin_repository: AdminRepository,
        feedback_repository: FeedbackRepository,
        guide_list_sender: GuideListSender,
    ) -> None:
        self.__completion_sender = FeedbackCompletionSender(guide_list_sender)
        self.__feedback_repository = feedback_repository
        self.__notifier = FeedbackAdminNotifier(admin_repository)
    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__send_feedback, F.data == FeedbackCallbackData.SEND_FEEDBACK
        )
        dispatcher.callback_query.register(
            self.__leave_feedback_later, F.data == FeedbackCallbackData.LEAVE_LATER
        )
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
            await self.__completion_sender.send_success(
                callback.message, callback.from_user.id
            )
    async def __leave_feedback_later(self, callback: CallbackQuery, state: FSMContext) -> None:
        await state.clear()
        await callback.answer()
        if callback.message is not None:
            await self.__completion_sender.send_later(
                callback.message, callback.from_user.id
            )
