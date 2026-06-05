from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.guides.keyboards import GuideKeyboardFactory
from src.messages.start_message import StartMessageProvider
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.services.post_sender import TelegramPostSender


class StartCommandHandler:
    def __init__(
        self,
        post_repository: PostRepository,
        media_repository: PostMediaRepository,
        user_repository: UserRepository,
        viz_price_rub: str = "",
    ) -> None:
        self.__message_provider = StartMessageProvider(post_repository, media_repository)
        self.__post_sender = TelegramPostSender()
        self.__keyboard_factory = GuideKeyboardFactory()
        self.__user_repository = user_repository
        self.__viz_price_rub = viz_price_rub

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__send_start_message, CommandStart())

    async def __send_start_message(self, message: Message) -> None:
        if message.from_user is not None:
            self.__user_repository.save_registered_user(message.from_user)
        await self.__post_sender.send_post(
            message,
            self.__message_provider.get_start_post(),
            self.__keyboard_factory.build_guide_selection_keyboard(self.__viz_price_rub),
        )
