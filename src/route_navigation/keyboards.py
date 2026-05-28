from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.route_navigation.button_text_resolver import RouteButtonTextResolver
from src.route_navigation.callbacks import RouteNavigationCallbackData


class RouteNavigationKeyboardFactory:
    def __init__(self) -> None:
        self.__callbacks = RouteNavigationCallbackData()
        self.__text_resolver = RouteButtonTextResolver()

    def build_next_post_keyboard(self, next_post_number: int) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=self.__text_resolver.resolve_button_text(next_post_number),
                        callback_data=self.__callbacks.build_post_callback(
                            next_post_number
                        ),
                    )
                ]
            ]
        )
