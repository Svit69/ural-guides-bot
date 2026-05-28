from aiogram import Dispatcher

from src.handlers.admin_photo_handler import AdminPhotoHandler
from src.handlers.admin_post_number_handler import AdminPostNumberHandler
from src.handlers.admin_text_decision_handler import AdminTextDecisionHandler
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_repository import PostRepository


class AdminContentEditHandler:
    def __init__(
        self, admin_repository: AdminRepository, post_repository: PostRepository
    ) -> None:
        self.__handlers = [
            AdminPostNumberHandler(admin_repository),
            AdminTextDecisionHandler(admin_repository, post_repository),
            AdminPhotoHandler(admin_repository, post_repository),
        ]

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        for handler in self.__handlers:
            handler.register_in_dispatcher(dispatcher)
