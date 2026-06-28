from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from src.guides.callbacks import GuideCallbackData


class ChekistsKeyboardFactory:
    def build_find_all_idols_keyboard(self) -> InlineKeyboardMarkup:
        button = InlineKeyboardButton(
            text="хочу найти всех",
            callback_data=GuideCallbackData.CHEKISTS_FIND_ALL_IDOLS,
        )
        return InlineKeyboardMarkup(inline_keyboard=[[button]])
