from aiogram.types import InlineKeyboardButton

from src.guides.callbacks import GuideCallbackData
from src.guides.guide_ids import GUIDE_BIG_KONNY, GUIDE_CHEKISTS
from src.guides.guide_ids import GUIDE_CITY_WALK, GUIDE_VIZ


class GuideSelectionRows:
    def build_rows(
        self, viz_text: str, city_text: str, visible_guides: set[str]
    ) -> list[list[InlineKeyboardButton]]:
        rows = []
        if GUIDE_VIZ in visible_guides:
            rows.append([self.__button(viz_text, GuideCallbackData.SELECT_VIZ)])
        if GUIDE_CITY_WALK in visible_guides:
            rows.append([self.__button(city_text, GuideCallbackData.SELECT_CITY_WALK)])
        if GUIDE_BIG_KONNY in visible_guides:
            rows.append([self.__button("Большой Конный п-ов", GuideCallbackData.SELECT_BIG_KONNY)])
        if GUIDE_CHEKISTS in visible_guides:
            rows.append([self.__button("Городок чекистов", GuideCallbackData.SELECT_CHEKISTS)])
        return rows

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
