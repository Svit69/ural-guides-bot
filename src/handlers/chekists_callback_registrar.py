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
            (handler._send_chekists_eighth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_SEVENTH),
            (handler._send_chekists_ninth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_EIGHTH),
            (handler._send_chekists_tenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_NINTH),
            (handler._send_chekists_eleventh_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TENTH),
            (handler._send_chekists_twelfth_post, GuideCallbackData.CHEKISTS_FIND_ALL_IDOLS),
            (handler._send_chekists_thirteenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWELFTH),
            (handler._send_chekists_fourteenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_THIRTEENTH),
            (handler._send_chekists_fifteenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_FOURTEENTH),
            (handler._send_chekists_sixteenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_FIFTEENTH),
            (handler._send_chekists_seventeenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_SIXTEENTH),
            (handler._send_chekists_eighteenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_SEVENTEENTH),
            (handler._send_chekists_nineteenth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_EIGHTEENTH),
            (handler._send_chekists_twentieth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_NINETEENTH),
            (handler._send_chekists_twenty_first_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTIETH),
            (handler._send_chekists_twenty_second_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_FIRST),
            (handler._send_chekists_twenty_third_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_SECOND),
            (handler._send_chekists_twenty_fourth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_THIRD),
            (handler._send_chekists_twenty_fifth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_FOURTH),
            (handler._send_chekists_twenty_sixth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_FIFTH),
            (handler._send_chekists_twenty_seventh_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_SIXTH),
            (handler._send_chekists_twenty_eighth_post, GuideCallbackData.CHEKISTS_NEXT_AFTER_TWENTY_SEVENTH),
        )
        for callback_handler, callback_data in pairs:
            dispatcher.callback_query.register(callback_handler, F.data == callback_data)
