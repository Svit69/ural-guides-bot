from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.callbacks import AdminCallbackData
from src.admin.states import AddAdminStates
from src.repositories.admin_repository import AdminRepository


class AdminAccessManagementHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__admin_repository = admin_repository

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(
            self.__request_admin_id, F.data == AdminCallbackData.ADD_ADMIN
        )
        dispatcher.message.register(
            self.__save_new_admin, AddAdminStates.waiting_for_telegram_id
        )

    async def __request_admin_id(
        self, callback: CallbackQuery, state: FSMContext
    ) -> None:
        await callback.answer()
        if not self.__guard.is_admin_callback(callback) or callback.message is None:
            return
        await state.set_state(AddAdminStates.waiting_for_telegram_id)
        await callback.message.answer("Отправьте Telegram ID нового администратора.")

    async def __save_new_admin(self, message: Message, state: FSMContext) -> None:
        if not self.__guard.is_admin_message(message):
            await state.clear()
            return
        try:
            telegram_id = int((message.text or "").strip())
        except ValueError:
            await message.answer("Telegram ID должен быть числом.")
            return
        self.__admin_repository.add_admin(telegram_id)
        await state.clear()
        await message.answer(f"Администратор {telegram_id} добавлен.")
