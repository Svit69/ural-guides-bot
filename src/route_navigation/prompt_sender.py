from aiogram.types import Message

from src.route_navigation.keyboards import RouteNavigationKeyboardFactory


class RouteNavigationPromptSender:
    def __init__(self) -> None:
        self.__keyboard_factory = RouteNavigationKeyboardFactory()

    async def send_next_post_prompt(self, message: Message) -> None:
        await message.answer(
            "Продолжим?",
            reply_markup=self.__keyboard_factory.build_next_post_keyboard(),
        )
