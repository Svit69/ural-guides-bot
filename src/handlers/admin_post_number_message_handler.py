from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.post_number_prompts import POST_GUIDE_ERROR_TEXT, POST_NUMBER_ERROR_TEXT
from src.admin.post_number_workflow import AdminPostNumberWorkflow
from src.admin.states import EditContentStates
from src.repositories.admin_repository import AdminRepository


class AdminPostNumberMessageHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__workflow = AdminPostNumberWorkflow()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(
            self.__receive_post_number, EditContentStates.waiting_for_post_number
        )

    async def __receive_post_number(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message):
            await state.clear()
            return
        post_number = self.__workflow.parse_post_number(message.text)
        if post_number is None:
            await message.answer(POST_NUMBER_ERROR_TEXT)
            return
        if not await self.__workflow.is_selected_guide_post(state, post_number):
            await message.answer(POST_GUIDE_ERROR_TEXT)
            return
        await self.__workflow.ask_text_decision(message, state, post_number)
