from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.guides.callbacks import GuideCallbackData
from src.guides.city_walk_post import CITY_WALK_POST_NUMBER
from src.messages.post_provider import PostProvider
from src.payments.city_keyboards import CityPaymentKeyboardFactory
from src.payments.city_messages import CITY_PAYMENT_NOT_CONFIGURED
from src.payments.city_messages import build_city_payment_error, build_city_payment_prompt
from src.payments.city_payment_service import CityPaymentService
from src.payments.exceptions import PaymentGatewayError
from src.handlers.city_payment_check_handler import CityPaymentCheckHandlerMixin
from src.repositories.admin_repository import AdminRepository
from src.services.city_walk_sender import CityWalkGuideSender


class CityPaymentHandler(CityPaymentCheckHandlerMixin):
    def __init__(self, payments: CityPaymentService, posts: PostProvider, admins: AdminRepository) -> None:
        self._payments = payments
        self._admins = admins
        self.__sender = CityWalkGuideSender(posts)
        self.__keyboards = CityPaymentKeyboardFactory()

    def register_in_dispatcher(self, dispatcher: Dispatcher) -> None:
        dispatcher.callback_query.register(self.__request_payment, F.data == GuideCallbackData.SELECT_CITY_WALK)
        dispatcher.callback_query.register(self._check_city_payment, F.data == GuideCallbackData.CHECK_CITY_PAYMENT)

    async def __request_payment(self, callback: CallbackQuery, state: FSMContext) -> None:
        await callback.answer()
        if callback.message is None:
            return
        if self._admins.is_admin(callback.from_user.id) or self._payments.has_local_access(callback.from_user.id):
            await self._send_city_guide(callback, state)
            return
        if not self._payments.is_configured():
            await callback.message.answer(CITY_PAYMENT_NOT_CONFIGURED)
            return
        try:
            if await self._payments.has_paid_access(callback.from_user.id):
                await self._notify_city_purchase(callback)
                await self._send_city_guide(callback, state)
                return
            payment = await self._payments.get_or_create_payment(callback.from_user.id)
        except PaymentGatewayError as error:
            await callback.message.answer(build_city_payment_error(error.public_reason))
            return
        keyboard = self.__keyboards.build_payment_keyboard(str(payment["confirmation_url"]))
        await callback.message.answer(build_city_payment_prompt(self._payments.get_price_rub()), reply_markup=keyboard)

    async def _send_city_guide(self, callback: CallbackQuery, state: FSMContext) -> None:
        if callback.message is not None:
            await self.__sender.send_guide(callback.message, CITY_WALK_POST_NUMBER, state)
