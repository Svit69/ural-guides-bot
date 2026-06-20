from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.feedback_cleanup_presenter import FeedbackCleanupPresenter
from src.admin.states import ClearFeedbackStates
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository


class AdminFeedbackCleanupStartHandler:
    def __init__(
        self, admin_repository: AdminRepository, feedback_repository: FeedbackRepository
    ) -> None:
        self.__feedback_repository = feedback_repository
        self.__guard = AdminAccessGuard(admin_repository)
        self.__presenter = FeedbackCleanupPresenter()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__start_cleanup, F.data == AdminCallbackData.CLEAR_FEEDBACK
        )

    async def __start_cleanup(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        feedback_items = self.__feedback_repository.get_all_feedback()
        if not feedback_items:
            await callback.message.answer("Отзывов пока нет.")
            return
        await state.set_state(ClearFeedbackStates.waiting_for_ids)
        await callback.message.answer(self.__presenter.build_numbered_list(feedback_items))
