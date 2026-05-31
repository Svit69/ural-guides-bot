from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory
from src.admin.photo_question_sender import PhotoQuestionSender
from src.admin.post_editor import AdminPostEditor
from src.admin.states import EditContentStates
from src.handlers.admin_text_receive_handler import AdminTextReceiveMixin
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository


class AdminTextDecisionHandler(AdminTextReceiveMixin):
    def __init__(self, admin_repository: AdminRepository, posts: PostRepository, media: PostMediaRepository) -> None:
        self._guard = AdminAccessGuard(admin_repository)
        self.__post_editor = AdminPostEditor(posts, media)
        self._photo_question_sender = PhotoQuestionSender()
        self.__keyboard_factory = AdminKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__keep_current_text, F.data == AdminCallbackData.KEEP_TEXT)
        dispatcher.callback_query.register(self.__request_replacement_text, F.data == AdminCallbackData.REPLACE_TEXT)
        dispatcher.message.register(self._receive_replacement_text, EditContentStates.waiting_for_replacement_text)

    async def __keep_current_text(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self._guard.is_admin_callback(callback) or callback.message is None:
            return
        post_number = (await state.get_data())["post_number"]
        post = self.__post_editor.get_editable_post(post_number)
        await state.update_data(text=post["text"])
        await self._photo_question_sender.ask_photo_question(callback.message, state)

    async def __request_replacement_text(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self._guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.set_state(EditContentStates.waiting_for_replacement_text)
        await callback.message.answer("Отправьте новый текст поста.", reply_markup=self.__keyboard_factory.build_cancel_keyboard())
