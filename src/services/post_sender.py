from aiogram.types import InlineKeyboardMarkup, Message

from src.services.media_group_builder import MediaGroupBuilder
from src.text_formatting.telegram_formatter import TelegramTextFormatter


class TelegramPostSender:
    __caption_limit = 1024

    def __init__(self) -> None:
        self.__formatter = TelegramTextFormatter()
        self.__media_group_builder = MediaGroupBuilder()

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
        await self.__send_media_post(message, media, formatted_text, reply_markup)

    async def __send_media_post(
        self,
        message: Message,
        media: list[dict[str, str]],
        formatted_text: str,
        reply_markup: InlineKeyboardMarkup | None,
    ) -> None:
        caption = formatted_text if len(formatted_text) <= self.__caption_limit else ""
        if len(media) == 1 and media[0]["media_type"] == "photo":
            await message.answer_photo(
                media[0]["file_id"], caption=caption, reply_markup=reply_markup
            )
        elif len(media) == 1:
            await message.answer_video(
                media[0]["file_id"], caption=caption, reply_markup=reply_markup
            )
        else:
            await message.answer_media_group(
                self.__media_group_builder.build_media_group(media, caption)
            )
        if not caption:
            await message.answer(
                formatted_text,
                disable_web_page_preview=True,
                reply_markup=reply_markup,
            )
