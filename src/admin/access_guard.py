from aiogram.types import CallbackQuery, Message

from src.repositories.admin_repository import AdminRepository


class AdminAccessGuard:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__admin_repository = admin_repository

    def is_admin_message(self, message: Message) -> bool:
        return bool(message.from_user and self.__admin_repository.is_admin(message.from_user.id))

    def is_admin_callback(self, callback: CallbackQuery) -> bool:
        return bool(callback.from_user and self.__admin_repository.is_admin(callback.from_user.id))
