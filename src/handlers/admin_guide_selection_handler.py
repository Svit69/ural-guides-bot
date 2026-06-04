from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory
from src.admin.post_number_prompts import GUIDE_SELECTION_PROMPT, POST_SELECTION_PROMPT
from src.admin.states import EditContentStates
from src.repositories.admin_repository import AdminRepository


class AdminGuideSelectionHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__keyboards = AdminKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__request_guide, F.data == AdminCallbackData.EDIT_CONTENT)
        dispatcher.callback_query.register(self.__select_guide, F.data.startswith(AdminCallbackData.SELECT_GUIDE_PREFIX))

    async def __request_guide(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.set_state(EditContentStates.waiting_for_guide)
        await callback.message.answer(GUIDE_SELECTION_PROMPT, reply_markup=self.__keyboards.build_guide_selection_keyboard())

    async def __select_guide(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        guide_id = AdminCallbackData.parse_guide_id(callback.data or "")
        if guide_id is None:
            return
        await state.update_data(guide_id=guide_id)
        await state.set_state(EditContentStates.waiting_for_post_number)
        await callback.message.answer(POST_SELECTION_PROMPT, reply_markup=self.__keyboards.build_post_selection_keyboard(guide_id))
