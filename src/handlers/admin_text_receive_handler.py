from aiogram.fsm.context import FSMContext
from aiogram.types import Message


class AdminTextReceiveMixin:
    async def _receive_replacement_text(
        self, message: Message, state: FSMContext
    ) -> None:
        if not self._guard.is_admin_message(message):
            await state.clear()
            return
        await state.update_data(text=message.text or "")
        await self._photo_question_sender.ask_photo_question(message, state)
