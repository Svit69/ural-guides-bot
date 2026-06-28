from aiogram.types import Message

from src.user_panel.keyboards import UserPanelKeyboardFactory
from src.user_panel.messages import USER_PANEL_TEXT


class UserPanelSender:
    def __init__(self) -> None:
        self.__keyboard = UserPanelKeyboardFactory()

    async def send_panel(self, message: Message) -> None:
        await message.answer(
            USER_PANEL_TEXT, reply_markup=self.__keyboard.build_main_keyboard()
        )
