from aiogram import Dispatcher

from src.handlers.admin_post_number_callback_handler import AdminPostNumberCallbackHandler
from src.handlers.admin_post_number_message_handler import AdminPostNumberMessageHandler
from src.repositories.admin_repository import AdminRepository


class AdminPostNumberHandler:
    def __init__(self, admin_repository: AdminRepository) -> None:
        self.__handlers = [
            AdminPostNumberCallbackHandler(admin_repository),
            AdminPostNumberMessageHandler(admin_repository),
        ]

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        for handler in self.__handlers:
            handler.register_in_dispatcher(dispatcher)
