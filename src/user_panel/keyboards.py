from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class UserPanelKeyboardFactory:
    def build_main_keyboard(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="все гайды")],
                [KeyboardButton(text="обратная связь")],
            ],
            resize_keyboard=True,
        )
