from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.photo_question_sender import PhotoQuestionSender
from src.admin.post_editor import AdminPostEditor
from src.admin.states import EditContentStates
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_repository import PostRepository


class AdminTextDecisionHandler:
    def __init__(self, admin_repository: AdminRepository, posts: PostRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__post_editor = AdminPostEditor(posts)
        self.__photo_question_sender = PhotoQuestionSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__keep_current_text, F.data == AdminCallbackData.KEEP_TEXT
        )
        dispatcher.callback_query.register(
            self.__request_replacement_text, F.data == AdminCallbackData.REPLACE_TEXT
        )
        dispatcher.message.register(
            self.__receive_replacement_text,
            EditContentStates.waiting_for_replacement_text,
        )

    async def __keep_current_text(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        post_number = (await state.get_data())["post_number"]
        post = self.__post_editor.get_editable_post(post_number)
        await state.update_data(text=post["text"])
        await self.__photo_question_sender.ask_photo_question(callback.message, state)

    async def __request_replacement_text(
        self, callback: CallbackQuery, state: FSMContext
    ) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.set_state(EditContentStates.waiting_for_replacement_text)
        await callback.message.answer("Отправьте новый текст поста.")

    async def __receive_replacement_text(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message):
            await state.clear()
            return
        await state.update_data(text=message.text or "")
        await self.__photo_question_sender.ask_photo_question(message, state)
