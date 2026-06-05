from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.guides.callbacks import GuideCallbackData


class GuideKeyboardFactory:
    def build_guide_selection_keyboard(self, viz_price_rub: str = "") -> InlineKeyboardMarkup:
        price = self.__format_price(viz_price_rub)
        viz_text = f"ВИЗ {price} 💳" if price else "ВИЗ 💳"
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [self.__button(viz_text, GuideCallbackData.SELECT_VIZ)],
                [self.__button("Большой Конный п-ов", GuideCallbackData.SELECT_BIG_KONNY)],
            ]
        )

    def build_viz_next_keyboard(
        self, callback_data: str = GuideCallbackData.VIZ_NEXT
    ) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[[self.__button("идем дальше", callback_data)]]
        )

    def build_viz_baby_head_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    self.__button(
                        "почему на пляже голова младенца?",
                        GuideCallbackData.VIZ_NEXT_AFTER_TWENTIETH,
                    )
                ]
            ]
        )

    def build_viz_finish_keyboard(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[[self.__button("завершить прогулку", GuideCallbackData.FINISH_VIZ)]]
        )

    def __button(self, text: str, callback_data: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callback_data)

    def __format_price(self, raw_price: str) -> str:
        normalized_price = raw_price.removesuffix(".00")
        return f"{normalized_price} ₽" if normalized_price else ""
