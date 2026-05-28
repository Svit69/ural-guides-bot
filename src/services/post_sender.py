from aiogram.types import Message

from src.text_formatting.telegram_formatter import TelegramTextFormatter


class TelegramPostSender:
    __caption_limit = 1024

    def __init__(self) -> None:
        self.__formatter = TelegramTextFormatter()

    async def send_post(self, message: Message, post: dict[str, str | None]) -> None:
        formatted_text = self.__formatter.format_text(str(post["text"]))
        photo_file_id = post.get("photo_file_id")
        if photo_file_id is None:
            await message.answer(formatted_text, disable_web_page_preview=True)
            return
        await self.__send_photo_post(message, photo_file_id, formatted_text)

    async def __send_photo_post(
        self, message: Message, photo_file_id: str, formatted_text: str
    ) -> None:
        if len(formatted_text) <= self.__caption_limit:
            await message.answer_photo(
                photo_file_id,
                caption=formatted_text,
            )
            return
        await message.answer_photo(photo_file_id)
        await message.answer(formatted_text, disable_web_page_preview=True)
