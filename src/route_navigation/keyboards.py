from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.route_navigation.callbacks import RouteNavigationCallbackData


class RouteNavigationKeyboardFactory:
    def build_next_post_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="идем дальше",
                        callback_data=RouteNavigationCallbackData.THIRD_POST,
                    )
                ]
            ]
        )
