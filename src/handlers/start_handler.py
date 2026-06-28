from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.messages.start_message import StartMessageProvider
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.repositories.city_access_repository import CityAccessRepository
from src.repositories.viz_access_repository import VizAccessRepository
from src.repositories.admin_repository import AdminRepository
from src.repositories.guide_visibility_repository import GuideVisibilityRepository
from src.services.start_guide_keyboard_builder import StartGuideKeyboardBuilder
from src.services.post_sender import TelegramPostSender
from src.user_panel.panel_sender import UserPanelSender

class StartCommandHandler:
    def __init__(
        self,
        post_repository: PostRepository,
        media_repository: PostMediaRepository,
        user_repository: UserRepository,
        viz_access_repository: VizAccessRepository,
        city_access_repository: CityAccessRepository,
        admin_repository: AdminRepository,
        visibility_repository: GuideVisibilityRepository,
        viz_price_rub: str = "",
        city_price_rub: str = "",
    ) -> None:
        self.__message_provider = StartMessageProvider(post_repository, media_repository)
        self.__post_sender = TelegramPostSender()
        self.__user_repository = user_repository
        self.__guide_keyboard_builder = StartGuideKeyboardBuilder(
            viz_access_repository, city_access_repository, admin_repository,
            visibility_repository, viz_price_rub, city_price_rub
        )
        self.__panel_sender = UserPanelSender()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__send_start_message, CommandStart())

    async def __send_start_message(self, message: Message) -> None:
        if message.from_user is not None:
            self.__user_repository.save_registered_user(message.from_user)
        user_id = message.from_user.id if message.from_user else 0
        await self.__post_sender.send_post(
            message,
            self.__message_provider.get_start_post(),
            self.__guide_keyboard_builder.build_for_user(user_id),
        )
        await self.__panel_sender.send_panel(message)
