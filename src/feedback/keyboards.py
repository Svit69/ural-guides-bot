from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.feedback.callbacks import FeedbackCallbackData


class FeedbackKeyboardFactory:
    def build_confirmation_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="отправить отзыв",
                        callback_data=FeedbackCallbackData.SEND_FEEDBACK,
                    )
                ]
            ]
        )
