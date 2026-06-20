from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.post_number_workflow import AdminPostNumberWorkflow
from src.repositories.admin_repository import AdminRepository


class AdminPostNumberCallbackHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__workflow = AdminPostNumberWorkflow()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__select_post_number,
            F.data.startswith(AdminCallbackData.SELECT_POST_PREFIX),
        )

    async def __select_post_number(
        self, callback: CallbackQuery, state: FSMContext
    ) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        post_number = AdminCallbackData.parse_post_number(callback.data or "")
        if post_number is None:
            return
        if await self.__workflow.is_selected_guide_post(state, post_number):
            await self.__workflow.ask_text_decision(callback.message, state, post_number)
