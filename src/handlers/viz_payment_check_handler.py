from aiogram.types import CallbackQuery

from src.payments.exceptions import PaymentGatewayError
from src.payments.messages import VIZ_PAYMENT_NOT_CONFIGURED, VIZ_PAYMENT_PENDING
from src.payments.messages import build_viz_payment_error


class VizPaymentCheckHandlerMixin:
    async def _check_payment(self, callback: CallbackQuery) -> None:
        if self._payments.has_local_access(callback.from_user.id):
            await callback.answer()
            if callback.message is not None:
                await self._send_first_post(callback)
            return
        if not self._payments.is_configured():
            await callback.answer(VIZ_PAYMENT_NOT_CONFIGURED, show_alert=True)
            return
        try:
            has_access = await self._payments.has_paid_access(callback.from_user.id)
        except PaymentGatewayError as error:
            await callback.answer(build_viz_payment_error(error.public_reason), show_alert=True)
            return
        await callback.answer("" if has_access else VIZ_PAYMENT_PENDING, show_alert=not has_access)
        if has_access and callback.message is not None:
            await self._send_first_post(callback)
