from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.guides.callbacks import GuideCallbackData


class GuideKeyboardFactory:
    def build_guide_selection_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button("ВИЗ 💳", GuideCallbackData.SELECT_VIZ)],
                [self.__button("Большой Конный п-ов", GuideCallbackData.SELECT_BIG_KONNY)],
            ]
        )

    def build_viz_next_keyboard(
        self, callback_data: str = GuideCallbackData.VIZ_NEXT
    ) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[[self.__button("идем дальше", callback_data)]]
        )

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
