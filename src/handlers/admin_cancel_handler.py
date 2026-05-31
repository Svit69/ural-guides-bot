from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.repositories.admin_repository import AdminRepository


class AdminCancelHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__cancel_by_button, F.data == AdminCallbackData.CANCEL)
        dispatcher.message.register(self.__cancel_by_command, F.text.casefold() == "/cancel")

    async def __cancel_by_button(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.clear()
        await callback.message.answer("Действие отменено. Изменения не сохранены.")

    async def __cancel_by_command(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message):
            return
        await state.clear()
        await message.answer("Действие отменено. Изменения не сохранены.")
