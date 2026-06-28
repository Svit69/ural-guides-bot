from aiogram import Dispatcher

from src.config.environment import EnvironmentSettings
from src.handlers.feedback_handler import FeedbackHandler
from src.handlers.start_handler import StartCommandHandler
from src.handlers.user_panel_handler import UserPanelHandler
from src.messages.post_provider import PostProvider
from src.repositories.admin_repository import AdminRepository
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.feedback_repository import FeedbackRepository
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.repositories.viz_access_repository import VizAccessRepository
from src.services.guide_list_sender import GuideListSender


class UserInteractionRegistrar:
    def __init__(self, settings: EnvironmentSettings) -> None:
        self.__settings = settings

    def register(self, dispatcher: Dispatcher, context: dict[str, object]) -> None:
        guide_list_sender = self.__create_guide_list_sender(context)
        StartCommandHandler(
            context["posts"], context["media"], context["users"],
            context["viz_access"], context["city_access"], context["admins"],
            context["guide_visibility"],
            self.__settings.viz_guide_price_rub,
            self.__settings.city_guide_price_rub,
        ).register_in_dispatcher(dispatcher)
        UserPanelHandler(guide_list_sender).register_in_dispatcher(dispatcher)
        FeedbackHandler(
            context["admins"], context["feedback"], guide_list_sender
        ).register_in_dispatcher(dispatcher)

    def __create_guide_list_sender(self, context: dict[str, object]) -> GuideListSender:
        return GuideListSender(
            context["viz_access"],
            context["city_access"],
            context["admins"],
            context["guide_visibility"],
            self.__settings.viz_guide_price_rub,
            self.__settings.city_guide_price_rub,
        )
