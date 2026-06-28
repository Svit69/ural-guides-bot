from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.guides.callbacks import GuideCallbackData
from src.guides.guide_button_texts import GuideButtonTextFactory
from src.guides.guide_ids import DEFAULT_VISIBLE_GUIDES
from src.guides.selection_rows import GuideSelectionRows

class GuideKeyboardFactory:
    def __init__(self) -> None:
        self.__rows = GuideSelectionRows()
        self.__texts = GuideButtonTextFactory()

    def build_guide_selection_keyboard(
        self,
        viz_price_rub: str = "",
        has_viz_access: bool = False,
        city_price_rub: str = "",
        has_city_access: bool = False,
        visible_guides: set[str] | None = None,
    ) -> InlineKeyboardMarkup:
        visible_guides = visible_guides or DEFAULT_VISIBLE_GUIDES
        viz_text = self.__texts.build_viz_text(viz_price_rub, has_viz_access)
        city_text = self.__texts.build_city_text(city_price_rub, has_city_access)
        return InlineKeyboardMarkup(
            inline_keyboard=self.__rows.build_rows(viz_text, city_text, visible_guides)
        )

    def build_viz_next_keyboard(self, callback_data: str = GuideCallbackData.VIZ_NEXT) -> InlineKeyboardMarkup:
        return self.__single_button_keyboard("идем дальше", callback_data)

    def build_viz_baby_head_keyboard(self) -> InlineKeyboardMarkup:
        text = "почему на пляже голова младенца?"
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button(text, GuideCallbackData.VIZ_NEXT_AFTER_TWENTIETH)]
            ]
        )

    def build_viz_finish_keyboard(self) -> InlineKeyboardMarkup:
        return self.__single_button_keyboard("завершить прогулку", GuideCallbackData.FINISH_VIZ)

    def build_chekists_next_keyboard(self) -> InlineKeyboardMarkup:
        return self.__single_button_keyboard("идем дальше", GuideCallbackData.CHEKISTS_NEXT)

    def __single_button_keyboard(self, text: str, callback_data: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[[self.__button(text, callback_data)]])

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
