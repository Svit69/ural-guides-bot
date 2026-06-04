from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.payments.exceptions import PaymentGatewayError
from src.payments.keyboards import VizPaymentKeyboardFactory
from src.payments.messages import VIZ_PAYMENT_ERROR, VIZ_PAYMENT_NOT_CONFIGURED
from src.payments.messages import VIZ_PAYMENT_PENDING, build_viz_payment_prompt
from src.payments.viz_payment_service import VizPaymentService
from src.services.post_sender import TelegramPostSender

class VizPaymentHandler:
    def __init__(self, payments: VizPaymentService, posts: PostProvider) -> None:
        self.__payments = payments
        self.__posts = posts
        self.__post_sender = TelegramPostSender()
        self.__payment_keyboards = VizPaymentKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__request_payment, F.data == GuideCallbackData.SELECT_VIZ)
        dispatcher.callback_query.register(self.__check_payment, F.data == GuideCallbackData.CHECK_VIZ_PAYMENT)

    async def __request_payment(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        if not self.__payments.is_configured():
            await callback.message.answer(VIZ_PAYMENT_NOT_CONFIGURED)
            return
        try:
            if await self.__payments.has_paid_access(callback.from_user.id):
                await self.__send_first_post(callback)
                return
            payment = await self.__payments.get_or_create_payment(callback.from_user.id)
        except PaymentGatewayError:
            await callback.message.answer(VIZ_PAYMENT_ERROR)
            return
        keyboard = self.__payment_keyboards.build_payment_keyboard(str(payment["confirmation_url"]))
        prompt = build_viz_payment_prompt(self.__payments.get_price_rub())
        await callback.message.answer(prompt, reply_markup=keyboard)

    async def __check_payment(self, callback: CallbackQuery) -> None:
        try:
            has_access = await self.__payments.has_paid_access(callback.from_user.id)
        except PaymentGatewayError:
            await callback.answer(VIZ_PAYMENT_ERROR, show_alert=True)
            return
        await callback.answer("" if has_access else VIZ_PAYMENT_PENDING, show_alert=not has_access)
        if has_access and callback.message is not None:
            await self.__send_first_post(callback)

    async def __send_first_post(self, callback: CallbackQuery) -> None:
        await self.__post_sender.send_post(callback.message, self.__posts.get_post(VIZ_FIRST_POST_NUMBER), GuideKeyboardFactory().build_viz_next_keyboard())
