from aiogram import Dispatcher, F
from src.guides.callbacks import GuideCallbackData


class ChekistsCallbackRegistrar:
    def register_callbacks(self, dispatcher: Dispatcher, handler: object) -> None:
        pairs = (
            (handler._send_chekists_second_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_FIRST),
            (handler._send_chekists_third_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_SECOND),
            (handler._send_chekists_fourth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRD),
            (handler._send_chekists_fifth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_FOURTH),
            (handler._send_chekists_sixth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_FIFTH),
            (handler._send_chekists_seventh_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_SIXTH),
        )
        for callback_handler, callback_data in pairs:
            dispatcher.callback_query.register(callback_handler, F.data == callback_data)
