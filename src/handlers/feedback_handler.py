from aiogram import Dispatcher

from src.handlers.feedback_callback_handler import FeedbackCallbackHandler
from src.handlers.feedback_message_handler import FeedbackMessageHandler
from src.repositories.admin_repository import AdminRepository
from src.repositories.feedback_repository import FeedbackRepository
from src.services.guide_list_sender import GuideListSender


class FeedbackHandler:
    def __init__(
        self,
        admin_repository: AdminRepository,
        feedback_repository: FeedbackRepository,
        guide_list_sender: GuideListSender,
    ) -> None:
        self.__handlers = [
            FeedbackMessageHandler(),
            FeedbackCallbackHandler(
                admin_repository, feedback_repository, guide_list_sender
            ),
        ]

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        for handler in self.__handlers:
            handler.register_in_dispatcher(dispatcher)
