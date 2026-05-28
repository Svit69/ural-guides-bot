from aiogram.types import Message

from src.feedback.keyboards import FeedbackKeyboardFactory
from src.feedback.messages import FEEDBACK_PREVIEW_TITLE


class FeedbackPreviewSender:
    def __init__(self) -> None:
        self.__keyboard_factory = FeedbackKeyboardFactory()

    async def send_preview(self, message: Message, payload: dict[str, object]) -> None:
        text = str(payload["text"] or "Медиа без подписи")
        caption = f"{FEEDBACK_PREVIEW_TITLE}\n\n{text}"
        media = payload.get("media")
        keyboard = self.__keyboard_factory.build_confirmation_keyboard()
        if media is None:
            await message.answer(caption, reply_markup=keyboard)
        elif media["media_type"] == "photo":
            await message.answer_photo(media["file_id"], caption=caption, reply_markup=keyboard)
        else:
            await message.answer_video(media["file_id"], caption=caption, reply_markup=keyboard)
