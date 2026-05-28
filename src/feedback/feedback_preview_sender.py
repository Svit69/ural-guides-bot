from aiogram.types import Message

from src.feedback.keyboards import FeedbackKeyboardFactory
from src.feedback.messages import FEEDBACK_PREVIEW_TITLE


class FeedbackPreviewSender:
    def __init__(self) -> None:
        self.__keyboard_factory = FeedbackKeyboardFactory()

    async def send_preview(self, message: Message, payload: dict[str, object]) -> None:
        text = str(payload["text"] or "Медиа без подписи")
        await message.answer(
            f"{FEEDBACK_PREVIEW_TITLE}\n\n{text}",
            reply_markup=self.__keyboard_factory.build_confirmation_keyboard(),
        )
