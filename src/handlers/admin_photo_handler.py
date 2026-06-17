from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.keyboards import AdminKeyboardFactory
from src.admin.media_item_extractor import MediaItemExtractor
from src.admin.post_editor import AdminPostEditor
from src.admin.states import EditContentStates
from src.handlers.admin_media_upload_handler import AdminMediaUploadMixin
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository


class AdminPhotoHandler(AdminMediaUploadMixin):
    def __init__(self, admin_repository: AdminRepository, posts: PostRepository, media: PostMediaRepository) -> None:
        self._guard = AdminAccessGuard(admin_repository)
        self._post_editor = AdminPostEditor(posts, media)
        self._media_extractor = MediaItemExtractor()
        self.__keyboard_factory = AdminKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__request_media, F.data == AdminCallbackData.ADD_PHOTO)
        dispatcher.callback_query.register(self._save_without_new_media, F.data == AdminCallbackData.SKIP_PHOTO)
        dispatcher.message.register(self._collect_uploaded_media, EditContentStates.waiting_for_media, F.photo | F.video | F.document)
        dispatcher.message.register(self._finish_media_upload, EditContentStates.waiting_for_media, F.text.casefold() == "готово")

    async def __request_media(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self._guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.update_data(media_items=[])
        await callback.message.answer(
            "Загрузите фото, видео или PDF. Когда закончите, напишите: готово",
            reply_markup=self.__keyboard_factory.build_cancel_keyboard(),
        )
