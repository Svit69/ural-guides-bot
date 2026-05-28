from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.messages.start_message import StartMessageProvider
from src.repositories.post_media_repository import PostMediaRepository
from src.repositories.post_repository import PostRepository
from src.repositories.user_repository import UserRepository
from src.services.post_sender import TelegramPostSender
from src.subscription.prompt_sender import SubscriptionPromptSender


class StartCommandHandler:
    def __init__(
        self,
        post_repository: PostRepository,
        media_repository: PostMediaRepository,
        user_repository: UserRepository,
    ) -> None:
        self.__message_provider = StartMessageProvider(post_repository, media_repository)
        self.__post_sender = TelegramPostSender()
        self.__subscription_prompt_sender = SubscriptionPromptSender()
        self.__user_repository = user_repository

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__send_start_message, CommandStart())

    async def __send_start_message(self, message: Message) -> None:
        if message.from_user is not None:
            self.__user_repository.save_registered_user(message.from_user)
        await self.__post_sender.send_post(
            message, self.__message_provider.get_start_post()
        )
        await self.__subscription_prompt_sender.send_subscription_prompt(message)
