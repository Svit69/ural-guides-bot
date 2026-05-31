from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.admin.callbacks import AdminCallbackData
from src.admin.post_selection import PostSelectionCatalog


class AdminKeyboardFactory:
    def build_main_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button("Пользователи", AdminCallbackData.USERS)],
                [self.__button("Показать все отзывы", AdminCallbackData.FEEDBACK)],
                [self.__button("Редактировать контент", AdminCallbackData.EDIT_CONTENT)],
                [self.__button("Добавить администратора", AdminCallbackData.ADD_ADMIN)],
            ]
        )

    def build_text_decision_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button("Оставить текст", AdminCallbackData.KEEP_TEXT)],
                [self.__button("Заменить текст", AdminCallbackData.REPLACE_TEXT)],
                [self.__cancel_button()],
            ]
        )

    def build_photo_decision_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button("Добавить медиа", AdminCallbackData.ADD_PHOTO)],
                [self.__button("Без новых медиа", AdminCallbackData.SKIP_PHOTO)],
                [self.__cancel_button()],
            ]
        )

    def build_post_selection_keyboard(self) -> InlineKeyboardMarkup:
        rows = [[self.__post_button(number, title)] for number, title in PostSelectionCatalog().get_items()]
        return InlineKeyboardMarkup(inline_keyboard=[*rows, [self.__cancel_button()]])

    def build_cancel_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[[self.__cancel_button()]])

    def __post_button(self, number: int, title: str) -> InlineKeyboardButton:
        return self.__button(f"{number}. {title}", AdminCallbackData.build_post_callback(number))

    def __cancel_button(self) -> InlineKeyboardButton:
        return self.__button("Отменить", AdminCallbackData.CANCEL)

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
