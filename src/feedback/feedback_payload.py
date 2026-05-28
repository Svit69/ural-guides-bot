from aiogram.types import Message

from src.admin.media_item_extractor import MediaItemExtractor


class FeedbackPayloadBuilder:
    def __init__(self) -> None:
        self.__media_extractor = MediaItemExtractor()

    def build_payload(self, message: Message) -> dict[str, object]:
        media_item = self.__media_extractor.extract_media_item(message)
        return {
            "text": message.text or message.caption or "",
            "media": media_item,
            "user_id": message.from_user.id if message.from_user else None,
            "full_name": message.from_user.full_name if message.from_user else "",
        }

    def is_empty(self, payload: dict[str, object]) -> bool:
        return not payload["text"] and payload["media"] is None
