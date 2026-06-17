from aiogram.types import InlineKeyboardButton

from src.admin.callbacks import AdminCallbackData


class AdminGuideKeyboardBuilder:
    def build_rows(self) -> list[list[InlineKeyboardButton]]:
        return [
            [self.__button("ВИЗ", AdminCallbackData.GUIDE_VIZ)],
            [self.__button("Прогулка по Екатеринбургу", AdminCallbackData.GUIDE_CITY_WALK)],
            [self.__button("Большой Конный п-ов", AdminCallbackData.GUIDE_BIG_KONNY)],
        ]

    def __button(self, text: str, guide_id: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            text=text, callback_data=AdminCallbackData.build_guide_callback(guide_id)
        )
