from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.admin.callbacks import AdminCallbackData


class AdminKeyboardFactory:
    def build_main_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Пользователи", callback_data=AdminCallbackData.USERS
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Редактировать контент",
                        callback_data=AdminCallbackData.EDIT_CONTENT,
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Добавить администратора",
                        callback_data=AdminCallbackData.ADD_ADMIN,
                    )
                ],
            ]
        )

    def build_text_decision_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Оставить текст", callback_data=AdminCallbackData.KEEP_TEXT)],
                [InlineKeyboardButton(text="Заменить текст", callback_data=AdminCallbackData.REPLACE_TEXT)],
            ]
        )

    def build_photo_decision_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Добавить фото", callback_data=AdminCallbackData.ADD_PHOTO)],
                [InlineKeyboardButton(text="Без нового фото", callback_data=AdminCallbackData.SKIP_PHOTO)],
            ]
        )
