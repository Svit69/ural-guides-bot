from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.guides.callbacks import GuideCallbackData
from src.guides.guide_button_texts import GuideButtonTextFactory


class GuideKeyboardFactory:
    def __init__(self) -> None:
        self.__texts = GuideButtonTextFactory()

    def build_guide_selection_keyboard(
        self,
        viz_price_rub: str = "",
        has_viz_access: bool = False,
        city_price_rub: str = "",
        has_city_access: bool = False,
    ) -> InlineKeyboardMarkup:
        viz_text = self.__texts.build_viz_text(viz_price_rub, has_viz_access)
        city_text = self.__texts.build_city_text(city_price_rub, has_city_access)
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button(viz_text, GuideCallbackData.SELECT_VIZ)],
                [self.__button(city_text, GuideCallbackData.SELECT_CITY_WALK)],
                [self.__button("Большой Конный п-ов", GuideCallbackData.SELECT_BIG_KONNY)],
            ]
        )

    def build_viz_next_keyboard(self, callback_data: str = GuideCallbackData.VIZ_NEXT) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[[self.__button("идем дальше", callback_data)]]
        )

    def build_viz_baby_head_keyboard(self) -> InlineKeyboardMarkup:
        text = "почему на пляже голова младенца?"
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button(text, GuideCallbackData.VIZ_NEXT_AFTER_TWENTIETH)]
            ]
        )

    def build_viz_finish_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[[self.__button("завершить прогулку", GuideCallbackData.FINISH_VIZ)]]
        )

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
