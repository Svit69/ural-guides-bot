from aiogram import Dispatcher

from src.handlers.admin_feedback_cleanup_selection_handler import AdminFeedbackCleanupSelectionHandler
from src.handlers.admin_feedback_cleanup_start_handler import AdminFeedbackCleanupStartHandler
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository


class AdminFeedbackCleanupHandler:
    def __init__(
        self, admin_repository: AdminRepository, feedback_repository: FeedbackRepository
    ) -> None:
        self.__handlers = [
            AdminFeedbackCleanupStartHandler(admin_repository, feedback_repository),
            AdminFeedbackCleanupSelectionHandler(admin_repository, feedback_repository),
        ]

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        for handler in self.__handlers:
            handler.register_in_dispatcher(dispatcher)
