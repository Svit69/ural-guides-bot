from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.feedback_sender import AdminFeedbackSender
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository


class AdminFeedbackHandler:
    def __init__(
        self, admin_repository: AdminRepository, feedback_repository: FeedbackRepository
    ) -> None:
        self.__feedback_repository = feedback_repository
        self.__feedback_sender = AdminFeedbackSender()
        self.__guard = AdminAccessGuard(admin_repository)

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__send_all_feedback, F.data == AdminCallbackData.FEEDBACK
        )

    async def __send_all_feedback(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        feedback_items = self.__feedback_repository.get_all_feedback()
        if not feedback_items:
            await callback.message.answer("Отзывов пока нет.")
            return
        for feedback in feedback_items:
            await self.__feedback_sender.send_feedback(callback.message, feedback)
