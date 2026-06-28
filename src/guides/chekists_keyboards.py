from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from src.guides.callbacks import GuideCallbackData


class ChekistsKeyboardFactory:
    def build_find_all_idols_keyboard(self) -> InlineKeyboardMarkup:
        return self.__single_button("хочу найти всех", GuideCallbackData.CHEKISTS_FIND_ALL_IDOLS)

    def build_second_idol_next_keyboard(self) -> InlineKeyboardMarkup:
        return self.__single_button("2/7 идем дальше", GuideCallbackData.CHEKISTS_NEXT_AFTER_FIFTEENTH)

    def build_third_idol_next_keyboard(self) -> InlineKeyboardMarkup:
        return self.__single_button("3/7 идем дальше", GuideCallbackData.CHEKISTS_NEXT)

    def __single_button(self, text: str, callback_data: str) -> InlineKeyboardMarkup:
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        return InlineKeyboardMarkup(inline_keyboard=[[button]])
