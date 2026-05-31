from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory
from src.admin.post_number_prompts import POST_NUMBER_ERROR_TEXT, POST_SELECTION_PROMPT
from src.admin.post_number_prompts import TEXT_DECISION_PROMPT
from src.admin.states import EditContentStates
from src.repositories.admin_repository import AdminRepository


class AdminPostNumberHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__keyboard_factory = AdminKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__request_post_number, F.data == AdminCallbackData.EDIT_CONTENT)
        dispatcher.callback_query.register(self.__select_post_number, F.data.startswith(AdminCallbackData.SELECT_POST_PREFIX))
        dispatcher.message.register(self.__receive_post_number, EditContentStates.waiting_for_post_number)

    async def __request_post_number(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.set_state(EditContentStates.waiting_for_post_number)
        await callback.message.answer(POST_SELECTION_PROMPT, reply_markup=self.__keyboard_factory.build_post_selection_keyboard())

    async def __select_post_number(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        post_number = AdminCallbackData.parse_post_number(callback.data or "")
        if post_number is not None:
            await self.__ask_text_decision(callback.message, state, post_number)

    async def __receive_post_number(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message):
            await state.clear()
            return
        post_number = self.__parse_post_number(message)
        if post_number is None:
            await message.answer(POST_NUMBER_ERROR_TEXT)
            return
        await self.__ask_text_decision(message, state, post_number)

    async def __ask_text_decision(self, message: Message, state: FSMContext, post_number: int) -> None:
        await state.update_data(post_number=post_number)
        await message.answer(TEXT_DECISION_PROMPT, reply_markup=self.__keyboard_factory.build_text_decision_keyboard())

    def __parse_post_number(self, message: Message) -> int | None:
        value = int(message.text.strip()) if message.text and message.text.strip().isdigit() else 0
        return value if value > 0 else None
