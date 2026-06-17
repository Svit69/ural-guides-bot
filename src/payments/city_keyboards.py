from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.guides.callbacks import GuideCallbackData


class CityPaymentKeyboardFactory:
    def build_payment_keyboard(self, payment_url: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Оплатить гайд", url=payment_url)],
                [
                    InlineKeyboardButton(
                        text="Проверить оплату",
                        callback_data=GuideCallbackData.CHECK_CITY_PAYMENT,
                    )
                ],
            ]
        )
