from aiogram import Dispatcher

from src.handlers.admin_access_handler import AdminAccessManagementHandler
from src.handlers.admin_content_handler import AdminContentEditHandler
from src.handlers.admin_panel_handler import AdminPanelCommandHandler
from src.handlers.admin_users_handler import AdminUsersHandler
from src.repositories.admin_repository import AdminRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository


class AdminPanelHandler:
    def __init__(
        self,
        admin_repository: AdminRepository,
        post_repository: PostRepository,
        user_repository: UserRepository,
    ) -> None:
        self.__handlers = [
            AdminPanelCommandHandler(admin_repository),
            AdminUsersHandler(admin_repository, user_repository),
            AdminAccessManagementHandler(admin_repository),
            AdminContentEditHandler(admin_repository, post_repository),
        ]

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        for handler in self.__handlers:
            handler.register_in_dispatcher(dispatcher)
