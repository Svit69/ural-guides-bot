from aiogram.types import InlineKeyboardMarkup, Message

from src.services.media_group_builder import MediaGroupBuilder


class MediaPostSender:
    __caption_limit = 1024

    def __init__(self) -> None:
        self.__media_group_builder = MediaGroupBuilder()

    async def send_media_post(
        self,
        message: Message,
        media: list[dict[str, str]],
        formatted_text: str,
        reply_markup: InlineKeyboardMarkup | None,
    ) -> None:
        caption = formatted_text if len(formatted_text) <= self.__caption_limit else ""
        if len(media) == 1:
            await self.__send_single_media(message, media[0], caption, reply_markup)
        elif reply_markup is not None:
            await self.__send_group_with_text_button(
                message, media, formatted_text, reply_markup
            )
        else:
            await self.__send_plain_group(message, media, caption)
        if not caption and reply_markup is None:
            await message.answer(formatted_text, disable_web_page_preview=True)

    async def __send_single_media(self, message, media_item, caption, reply_markup):
        if media_item["media_type"] == "photo":
            await message.answer_photo(
                media_item["file_id"], caption=caption, reply_markup=reply_markup
            )
            return
        await message.answer_video(
            media_item["file_id"], caption=caption, reply_markup=reply_markup
        )

    async def __send_group_with_text_button(self, message, media, text, reply_markup):
        await message.answer_media_group(self.__media_group_builder.build_media_group(media))
        await message.answer(text, disable_web_page_preview=True, reply_markup=reply_markup)

    async def __send_plain_group(self, message, media, caption) -> None:
        await message.answer_media_group(
            self.__media_group_builder.build_media_group(media, caption)
        )
