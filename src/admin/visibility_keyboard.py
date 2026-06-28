from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.admin.callbacks import AdminCallbackData
from src.admin.guide_titles import GUIDE_TITLES


class GuideVisibilityKeyboardFactory:
    def build_keyboard(self, visibility_map: dict[str, bool]) -> InlineKeyboardMarkup:
        rows = []
        for guide_id, title in GUIDE_TITLES.items():
            status = "виден" if visibility_map.get(guide_id, False) else "скрыт"
            rows.append([self.__button(f"{title}: {status}", guide_id)])
        rows.append([InlineKeyboardButton(text="Отменить", callback_data=AdminCallbackData.CANCEL)])
        return InlineKeyboardMarkup(inline_keyboard=rows)

    def __button(self, text: str, guide_id: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            text=text,
            callback_data=AdminCallbackData.build_toggle_guide_callback(guide_id),
        )
