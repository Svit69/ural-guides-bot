from aiogram.types import Message


class MediaItemExtractor:
    def extract_media_item(self, message: Message) -> dict[str, str] | None:
        if message.photo:
            return {"media_type": "photo", "file_id": message.photo[-1].file_id}
        if message.video:
            return {"media_type": "video", "file_id": message.video.file_id}
        if message.document and message.document.mime_type == "application/pdf":
            return {"media_type": "document", "file_id": message.document.file_id}
        return None
