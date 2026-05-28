from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.post_editor import AdminPostEditor
from src.admin.states import EditContentStates
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_repository import PostRepository


class AdminPhotoHandler:
    def __init__(self, admin_repository: AdminRepository, posts: PostRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__post_editor = AdminPostEditor(posts)

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__request_photo, F.data == AdminCallbackData.ADD_PHOTO
        )
        dispatcher.callback_query.register(
            self.__save_without_new_photo, F.data == AdminCallbackData.SKIP_PHOTO
        )
        dispatcher.message.register(
            self.__save_uploaded_photo, EditContentStates.waiting_for_photo, F.photo
        )

    async def __request_photo(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        await callback.message.answer("Загрузите фотографию для поста.")

    async def __save_without_new_photo(
        self, callback: CallbackQuery, state: FSMContext
    ) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        data = await state.get_data()
        self.__post_editor.save_post_with_existing_photo(data["post_number"], data["text"])
        await state.clear()
        await callback.message.answer("Пост сохранен без новой фотографии.")

    async def __save_uploaded_photo(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message) or not message.photo:
            await state.clear()
            return
        data = await state.get_data()
        self.__post_editor.save_post_with_new_photo(
            data["post_number"], data["text"], message.photo[-1].file_id
        )
        await state.clear()
        await message.answer("Пост сохранен с фотографией.")
