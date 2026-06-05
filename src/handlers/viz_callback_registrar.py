from aiogram import Dispatcher, F

from src.guides.callbacks import GuideCallbackData


class VizCallbackRegistrar:
    def register_route_callbacks(self, dispatcher: Dispatcher, handler: object) -> None:
        self.__register_early_route_callbacks(dispatcher, handler)
        self.__register_late_route_callbacks(dispatcher, handler)

    def __register_early_route_callbacks(self, dispatcher: Dispatcher, handler: object) -> None:
        dispatcher.callback_query.register(handler._send_viz_third_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SECOND)
        dispatcher.callback_query.register(handler._send_viz_fourth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_THIRD)
        dispatcher.callback_query.register(handler._send_viz_fifth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_FOURTH)
        dispatcher.callback_query.register(handler._send_viz_sixth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_FIFTH)
        dispatcher.callback_query.register(handler._send_viz_seventh_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SIXTH)
        dispatcher.callback_query.register(handler._send_viz_eighth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SEVENTH)

    def __register_late_route_callbacks(self, dispatcher: Dispatcher, handler: object) -> None:
        dispatcher.callback_query.register(handler._send_viz_ninth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_EIGHTH)
        dispatcher.callback_query.register(handler._send_viz_tenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_NINTH)
        dispatcher.callback_query.register(handler._send_viz_eleventh_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TENTH)
        dispatcher.callback_query.register(handler._send_viz_twelfth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_ELEVENTH)
        dispatcher.callback_query.register(handler._send_viz_thirteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWELFTH)
        dispatcher.callback_query.register(handler._send_viz_fourteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_THIRTEENTH)
        dispatcher.callback_query.register(handler._send_viz_fifteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_FOURTEENTH)
        dispatcher.callback_query.register(handler._send_viz_sixteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_FIFTEENTH)
        dispatcher.callback_query.register(handler._send_viz_seventeenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SIXTEENTH)
        dispatcher.callback_query.register(handler._send_viz_eighteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_SEVENTEENTH)
        dispatcher.callback_query.register(handler._send_viz_nineteenth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_EIGHTEENTH)
        dispatcher.callback_query.register(handler._send_viz_twentieth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_NINETEENTH)
        dispatcher.callback_query.register(handler._send_viz_twenty_first_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWENTIETH)
        dispatcher.callback_query.register(handler._send_viz_twenty_second_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_FIRST)
        dispatcher.callback_query.register(handler._send_viz_twenty_third_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_SECOND)
        dispatcher.callback_query.register(handler._send_viz_twenty_fourth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_THIRD)
        dispatcher.callback_query.register(handler._send_viz_twenty_fifth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_FOURTH)
        dispatcher.callback_query.register(handler._send_viz_twenty_sixth_post, F.data == GuideCallbackData.VIZ_NEXT_AFTER_TWENTY_FIFTH)
