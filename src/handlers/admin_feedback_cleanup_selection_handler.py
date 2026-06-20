from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.feedback_cleanup_keyboards import FeedbackCleanupKeyboardFactory
from src.admin.feedback_cleanup_presenter import FeedbackCleanupPresenter
from src.admin.feedback_id_parser import FeedbackIdParser
from src.admin.states import ClearFeedbackStates
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository

class AdminFeedbackCleanupSelectionHandler:
    def __init__(
        self, admin_repository: AdminRepository, feedback_repository: FeedbackRepository
    ) -> None:
        self.__feedback_repository = feedback_repository
        self.__guard = AdminAccessGuard(admin_repository)
        self.__keyboards = FeedbackCleanupKeyboardFactory()
        self.__parser = FeedbackIdParser()
        self.__presenter = FeedbackCleanupPresenter()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__receive_ids, ClearFeedbackStates.waiting_for_ids)
        dispatcher.callback_query.register(
            self.__confirm_cleanup, F.data == AdminCallbackData.CONFIRM_CLEAR_FEEDBACK
        )

    async def __receive_ids(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message):
            return
        feedback_ids = self.__parser.parse_ids(message.text)
        if not feedback_ids:
            await message.answer("Напишите номера отзывов через запятую.")
            return
        await state.update_data(feedback_ids=feedback_ids)
        await state.set_state(ClearFeedbackStates.waiting_for_confirmation)
        await message.answer(
            self.__presenter.build_confirmation_text(feedback_ids),
            reply_markup=self.__keyboards.build_confirmation_keyboard(),
        )

    async def __confirm_cleanup(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        data = await state.get_data()
        deleted_count = self.__feedback_repository.delete_feedback_by_ids(data.get("feedback_ids", []))
        await state.clear()
        await callback.message.answer(f"Удалено отзывов: {deleted_count}.")
