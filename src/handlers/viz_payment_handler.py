from aiogram import Dispatcher, F
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.keyboards import GuideKeyboardFactory
from src.guides.viz_posts import VIZ_FIRST_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.payments.exceptions import PaymentGatewayError
from src.payments.keyboards import VizPaymentKeyboardFactory
from src.payments.messages import VIZ_PAYMENT_NOT_CONFIGURED
from src.payments.messages import build_viz_payment_error
from src.payments.messages import build_viz_payment_prompt
from src.payments.viz_payment_service import VizPaymentService
from src.handlers.viz_payment_check_handler import VizPaymentCheckHandlerMixin
from src.repositories.admin_repository import AdminRepository
from src.services.post_sender import TelegramPostSender

class VizPaymentHandler(VizPaymentCheckHandlerMixin):
    def __init__(self, payments: VizPaymentService, posts: PostProvider, admins: AdminRepository) -> None:
        self._payments = payments
        self._admin_repository = admins
        self.__posts = posts
        self.__post_sender = TelegramPostSender()
        self.__payment_keyboards = VizPaymentKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__request_payment, F.data == GuideCallbackData.SELECT_VIZ)
        dispatcher.callback_query.register(self._check_payment, F.data == GuideCallbackData.CHECK_VIZ_PAYMENT)

    async def __request_payment(self, callback: CallbackQuery) -> None:
        await callback.answer()
        if callback.message is None:
            return
        if self._admin_repository.is_admin(callback.from_user.id) or self._payments.has_local_access(callback.from_user.id):
            await self._send_first_post(callback)
            return
        if not self._payments.is_configured():
            await callback.message.answer(VIZ_PAYMENT_NOT_CONFIGURED)
            return
        try:
            if await self._payments.has_paid_access(callback.from_user.id):
                await self._notify_viz_purchase(callback)
                await self._send_first_post(callback)
                return
            payment = await self._payments.get_or_create_payment(callback.from_user.id)
        except PaymentGatewayError as error:
            await callback.message.answer(build_viz_payment_error(error.public_reason))
            return
        keyboard = self.__payment_keyboards.build_payment_keyboard(str(payment["confirmation_url"]))
        await callback.message.answer(build_viz_payment_prompt(self._payments.get_price_rub()), reply_markup=keyboard)

    async def _send_first_post(self, callback: CallbackQuery) -> None:
        await self.__post_sender.send_post(callback.message, self.__posts.get_post(VIZ_FIRST_POST_NUMBER), GuideKeyboardFactory().build_viz_next_keyboard())
