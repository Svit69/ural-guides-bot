from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.payments.city_messages import CITY_PAYMENT_NOT_CONFIGURED, CITY_PAYMENT_PENDING
from src.payments.city_messages import build_city_payment_error
from src.payments.exceptions import PaymentGatewayError


class CityPaymentCheckHandlerMixin:
    async def _check_city_payment(self, callback: CallbackQuery, state: FSMContext) -> None:
        if self._admins.is_admin(callback.from_user.id):
            await callback.answer()
            await self._send_city_guide(callback, state)
            return
        if self._payments.has_local_access(callback.from_user.id):
            await callback.answer()
            await self._send_city_guide(callback, state)
            return
        if not self._payments.is_configured():
            await callback.answer(CITY_PAYMENT_NOT_CONFIGURED, show_alert=True)
            return
        try:
            has_access = await self._payments.has_paid_access(callback.from_user.id)
        except PaymentGatewayError as error:
            await callback.answer(build_city_payment_error(error.public_reason), show_alert=True)
            return
        await callback.answer("" if has_access else CITY_PAYMENT_PENDING, show_alert=not has_access)
        if has_access:
            await self._send_city_guide(callback, state)
