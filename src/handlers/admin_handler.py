from aiogram import Dispatcher

from src.handlers.admin_access_handler import AdminAccessManagementHandler
from src.handlers.admin_cancel_handler import AdminCancelHandler
from src.handlers.admin_content_handler import AdminContentEditHandler
from src.handlers.admin_feedback_handler import AdminFeedbackHandler
from src.handlers.admin_panel_handler import AdminPanelCommandHandler
from src.handlers.admin_users_handler import AdminUsersHandler
from src.handlers.admin_viz_buyers_handler import AdminVizBuyersHandler
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.repositories.viz_access_repository import VizAccessRepository


class AdminPanelHandler:
    def __init__(
        self,
        admin_repository: AdminRepository,
        feedback_repository: FeedbackRepository,
        post_repository: PostRepository,
        media_repository: PostMediaRepository,
        user_repository: UserRepository,
        viz_access_repository: VizAccessRepository,
    ) -> None:
        self.__handlers = [
            AdminCancelHandler(admin_repository),
            AdminPanelCommandHandler(admin_repository),
            AdminUsersHandler(admin_repository, user_repository, viz_access_repository),
            AdminVizBuyersHandler(admin_repository, viz_access_repository),
            AdminFeedbackHandler(admin_repository, feedback_repository),
            AdminAccessManagementHandler(admin_repository),
            AdminContentEditHandler(admin_repository, post_repository, media_repository),
        ]

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        for handler in self.__handlers:
            handler.register_in_dispatcher(dispatcher)
