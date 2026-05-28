from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.route_navigation.callbacks import RouteNavigationCallbackData


class RouteNavigationKeyboardFactory:
    def __init__(self) -> None:
        self.__callbacks = RouteNavigationCallbackData()

    def build_next_post_keyboard(self, next_post_number: int) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="идем дальше",
                        callback_data=self.__callbacks.build_post_callback(
                            next_post_number
                        ),
                    )
                ]
            ]
        )
