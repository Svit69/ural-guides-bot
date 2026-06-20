from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.admin.callbacks import AdminCallbackData


class FeedbackCleanupKeyboardFactory:
    def build_confirmation_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Удалить выбранные отзывы",
                        callback_data=AdminCallbackData.CONFIRM_CLEAR_FEEDBACK,
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Отменить",
                        callback_data=AdminCallbackData.CANCEL,
                    )
                ],
            ]
        )
