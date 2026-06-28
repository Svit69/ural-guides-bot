from aiogram.types import InlineKeyboardButton

from src.admin.callbacks import AdminCallbackData
from src.admin.guide_titles import GUIDE_TITLES


class AdminGuideKeyboardBuilder:
    def build_rows(self) -> list[list[InlineKeyboardButton]]:
        return [
            [self.__button(title, guide_id)] for guide_id, title in GUIDE_TITLES.items()
        ]

    def __button(self, text: str, guide_id: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            text=text, callback_data=AdminCallbackData.build_guide_callback(guide_id)
        )
