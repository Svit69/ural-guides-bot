from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.visibility_keyboard import GuideVisibilityKeyboardFactory
from src.repositories.admin_repository import AdminRepository
from src.repositories.guide_visibility_repository import GuideVisibilityRepository


class AdminGuideVisibilityHandler:
    def __init__(self, admins: AdminRepository, guides: GuideVisibilityRepository) -> None:
        self.__guard = AdminAccessGuard(admins)
        self.__guides = guides
        self.__keyboards = GuideVisibilityKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__show_panel, F.data == AdminCallbackData.GUIDE_VISIBILITY)
        dispatcher.callback_query.register(self.__toggle, F.data.startswith(AdminCallbackData.TOGGLE_GUIDE_PREFIX))

    async def __show_panel(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if self.__guard.is_admin_callback(callback) and callback.message is not None:
            await self.__send_panel(callback)

    async def __toggle(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        guide_id = (callback.data or "").removeprefix(AdminCallbackData.TOGGLE_GUIDE_PREFIX)
        self.__guides.toggle_visibility(guide_id)
        await self.__send_panel(callback)

    async def __send_panel(self, callback: CallbackQuery) -> None:
        await callback.message.answer(
            "Выберите, какие гайды показывать пользователям.",
            reply_markup=self.__keyboards.build_keyboard(self.__guides.get_visibility_map()),
        )
