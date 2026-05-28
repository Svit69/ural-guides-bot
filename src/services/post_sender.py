from aiogram.types import InlineKeyboardMarkup, Message

from src.services.media_post_sender import MediaPostSender
from src.text_formatting.telegram_formatter import TelegramTextFormatter


class TelegramPostSender:
    def __init__(self) -> None:
        self.__formatter = TelegramTextFormatter()
        self.__media_sender = MediaPostSender()

    async def send_post(
        self,
        message: Message,
        post: dict[str, object],
        reply_markup: InlineKeyboardMarkup | None = None,
    ) -> None:
        formatted_text = self.__formatter.format_text(str(post["text"]))
        media = list(post.get("media", []))
        if not media:
            await message.answer(
                formatted_text,
                disable_web_page_preview=True,
                reply_markup=reply_markup,
            )
            return
        await self.__media_sender.send_media_post(
            message, media, formatted_text, reply_markup
        )
