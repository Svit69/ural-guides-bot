from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.admin.message_text_extractor import AdminMessageTextExtractor


class AdminTextReceiveMixin:
    _text_extractor = AdminMessageTextExtractor()

    async def _receive_replacement_text(
        self, message: Message, state: FSMContext
    ) -> None:
        if not self._guard.is_admin_message(message):
            await state.clear()
            return
        await state.update_data(text=self._text_extractor.extract_editable_text(message))
        await self._photo_question_sender.ask_photo_question(message, state)
