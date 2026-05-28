from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from src.admin.access_guard import AdminAccessGuard
from src.admin.keyboards import AdminKeyboardFactory
from src.repositories.admin_repository import AdminRepository


class AdminPanelCommandHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__guard = AdminAccessGuard(admin_repository)
        self.__keyboard_factory = AdminKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__show_admin_panel, Command("admin"))

    async def __show_admin_panel(self, message: Message) -> None:
        if not self.__guard.is_admin_message(message):
            await message.answer("У вас нет доступа к админ-панели.")
            return
        await message.answer(
            "Админ-панель",
            reply_markup=self.__keyboard_factory.build_main_keyboard(),
        )
