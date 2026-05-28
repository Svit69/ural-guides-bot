from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.admin.callbacks import AdminCallbackData


class AdminKeyboardFactory:
    def build_main_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__build_button("Пользователи", AdminCallbackData.USERS)],
                [self.__build_button("Показать все отзывы", AdminCallbackData.FEEDBACK)],
                [self.__build_button("Редактировать контент", AdminCallbackData.EDIT_CONTENT)],
                [self.__build_button("Добавить администратора", AdminCallbackData.ADD_ADMIN)],
            ]
        )

    def build_text_decision_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__build_button("Оставить текст", AdminCallbackData.KEEP_TEXT)],
                [self.__build_button("Заменить текст", AdminCallbackData.REPLACE_TEXT)],
            ]
        )

    def build_photo_decision_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__build_button("Добавить медиа", AdminCallbackData.ADD_PHOTO)],
                [self.__build_button("Без новых медиа", AdminCallbackData.SKIP_PHOTO)],
            ]
        )

    def __build_button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)
