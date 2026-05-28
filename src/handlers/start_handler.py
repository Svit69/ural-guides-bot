from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.messages.start_message import StartMessageProvider
from src.text_formatting.telegram_formatter import TelegramTextFormatter


class StartCommandHandler:
    def __init__(self) -> None:
        self.__message_provider = StartMessageProvider()
        self.__formatter = TelegramTextFormatter()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.message.register(self.__send_start_message, CommandStart())

    async def __send_start_message(self, message: Message) -> None:
        formatted_text = self.__formatter.format_text(
            self.__message_provider.get_start_message()
        )
        await message.answer(formatted_text, disable_web_page_preview=True)
