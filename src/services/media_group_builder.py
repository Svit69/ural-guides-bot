from aiogram.types import InputMediaPhoto, InputMediaVideo


class MediaGroupBuilder:
    def build_media_group(self, media: list[dict[str, str]], caption: str = "") -> list:
        group = []
        for index, item in enumerate(media):
            group.append(self.__build_media_item(item, caption if index == 0 else ""))
        return group

    def __build_media_item(self, item: dict[str, str], caption: str):
        if item["media_type"] == "video":
            return InputMediaVideo(media=item["file_id"], caption=caption)
        return InputMediaPhoto(media=item["file_id"], caption=caption)
